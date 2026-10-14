import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector as sql
from datetime import datetime

class Penitenziario(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Penitenziario")
        self.geometry("1200x1000")
        self.__tempo = datetime.now().strftime("%H:%M:%S")
        self.__con = sql.connect(host="localhost",
                               user="root",
                               passwd="",
                               database="penitenziario")
        self.__cur = self.__con.cursor()

        self.__sezioni = {}
        self.__cortili = []
        self.__mense = []
        self.__tipo_localita_selezionata = ""
        self.__id_localita_selezionata = ""
        self.__id_carcerato_corrente = None
        self.__id_personale_corrente = None

        self.ottieni_tutti_i_dati()
        self.distribuisci_carcerati_nelle_celle()
        self.creaWidget()
        self.lM()
        self.inizializza_dati_e_ui()
        self.controlla_e_distribuisci()

        self.mainloop()

    def ottieni_celle(self):
        self.__cur.execute("SELECT id_cella, capienza FROM cella")
        return {row[0]: row[1] for row in self.__cur.fetchall()}

    def ottieni_cortili(self):
        self.__cur.execute("SELECT id_cortile, area FROM cortile")
        return [f"{row[0]} - {row[1]}" for row in self.__cur.fetchall()]

    def ottieni_id_cortili(self):
        self.__cur.execute("SELECT id_cortile FROM cortile")
        return [row[0] for row in self.__cur.fetchall()]

    def ottieni_mense(self):
        self.__cur.execute("SELECT id_mensa, menu FROM mensa")
        return [f"{row[0]} - {row[1]}" for row in self.__cur.fetchall()]

    def ottieni_id_mense(self):
        self.__cur.execute("SELECT id_mensa FROM mensa")
        return [row[0] for row in self.__cur.fetchall()]

    def ottieni_carcerati(self, tipo_localita=None, id_localita=None):
        query = "SELECT id_carc, nome, cognome, locType, locId FROM carcerato"
        if tipo_localita and id_localita:
            tipo_map = {"cella": "Cella", "cortile": "Cortile", "mensa": "Mensa"}
            if tipo_localita in tipo_map:
                query += f" WHERE locType = '{tipo_map[tipo_localita]}' AND locId = %s"
                self.__cur.execute(query, (id_localita,))
                carcerati_data = self.__cur.fetchall()
                return [f"{row[0]} - {row[1]} {row[2]}" for row in carcerati_data]
        self.__cur.execute(query)
        return [f"{row[0]} - {row[1]} {row[2]}" for row in self.__cur.fetchall()]

    def ottieni_personale(self):
        self.__cur.execute("SELECT id_pers, nome, cognome, ruolo FROM personale")
        return [f"{row[0]} - {row[1]} {row[2]} ({row[3]})" for row in self.__cur.fetchall()]

    def ottieni_turni(self):
        self.__cur.execute("SELECT t.id_turno, p.nome, p.cognome, t.inizio, t.fine FROM turno t JOIN personale p ON t.id_pers = p.id_pers ORDER BY t.inizio DESC")
        return self.__cur.fetchall()

    def ottieni_dati_carcerato(self, id_carcerato):
        self.__cur.execute("SELECT nome, cognome, locType, locId FROM carcerato WHERE id_carc = %s", (id_carcerato,))
        row = self.__cur.fetchone()
        return {'nome': row[0], 'cognome': row[1], 'tipo_localita_corrente': row[2], 'id_localita_corrente': row[3]} if row else {}
    
    def ottieni_dati_personale(self, id_personale):
        self.__cur.execute("SELECT nome, cognome, ruolo, dotazione FROM personale WHERE id_pers = %s", (id_personale,))
        row = self.__cur.fetchone()
        return {'nome': row[0], 'cognome': row[1], 'ruolo': row[2], 'dotazione': row[3]} if row else {}

    def ottieni_tutti_i_dati(self):
        self.__sezioni = self.ottieni_celle()
        self.__cortili = self.ottieni_cortili()
        self.__mense = self.ottieni_mense()
        self.ottieni_carcerati()

    def distribuisci_carcerati_nelle_celle(self):
        self.__cur.execute("SELECT id_carc FROM carcerato WHERE locType = 'Cella' OR locType IS NULL")
        unassigned_carcerati_ids = [row[0] for row in self.__cur.fetchall()]
        cella_occupancy = {cell_id: 0 for cell_id in self.__sezioni.keys()}
        self.__cur.execute("SELECT locId, COUNT(*) FROM carcerato WHERE locType = 'Cella' AND locId IS NOT NULL GROUP BY locId")
        for cell_id, count in self.__cur.fetchall():
            if cell_id in cella_occupancy:
                cella_occupancy[cell_id] = count
        carcerati_index = 0
        for cell_id, capienza in self.__sezioni.items():
            while cella_occupancy[cell_id] < capienza and carcerati_index < len(unassigned_carcerati_ids):
                carc_id = unassigned_carcerati_ids[carcerati_index]
                try:
                    self.__cur.execute("UPDATE carcerato SET locType = 'Cella', locId = %s WHERE id_carc = %s",
                                       (cell_id, carc_id))
                    self.__con.commit()
                    cella_occupancy[cell_id] += 1
                    carcerati_index += 1
                except sql.Error as err:
                    print(f"Errore durante l'assegnazione del carcerato {carc_id} alla cella {cell_id}: {err}")
        self.ottieni_carcerati()

    def distribuisci_carcerati_nelle_mense(self):
        self.__cur.execute("SELECT id_carc, locId FROM carcerato WHERE locType = 'Cella'")
        carcerati_data = self.__cur.fetchall()
        if not carcerati_data:
            return
        id_mense = self.ottieni_id_mense()
        if len(id_mense) < 2:
            return
        carcerati_ids = [row[0] for row in carcerati_data]
        metà = len(carcerati_ids) // 2
        prima_metà = carcerati_ids[:metà]
        seconda_metà = carcerati_ids[metà:]
        try:
            for carc_id in prima_metà:
                self.__cur.execute("UPDATE carcerato SET locType = 'Mensa', locId = %s WHERE id_carc = %s",
                                   (id_mense[0], carc_id))
            for carc_id in seconda_metà:
                self.__cur.execute("UPDATE carcerato SET locType = 'Mensa', locId = %s WHERE id_carc = %s",
                                   (id_mense[1], carc_id))
            self.__con.commit()
            self.ottieni_carcerati()
        except sql.Error as err:
            print(f"Errore durante la distribuzione nelle mense: {err}")

    def distribuisci_carcerati_nei_cortili(self):
        self.__cur.execute("SELECT id_carc FROM carcerato WHERE locType = 'Cella'")
        carcerati_ids = [row[0] for row in self.__cur.fetchall()]
        if not carcerati_ids:
            return
        id_cortili = self.ottieni_id_cortili()
        if not id_cortili:
            return
        cortile_id = id_cortili[0]
        try:
            for carc_id in carcerati_ids:
                self.__cur.execute("UPDATE carcerato SET locType = 'Cortile', locId = %s WHERE id_carc = %s",
                                   (cortile_id, carc_id))
            self.__con.commit()
            self.ottieni_carcerati()
        except sql.Error as err:
            print(f"Errore durante la distribuzione nei cortili: {err}")

    def riporta_carcerati_nelle_celle(self):
        self.__cur.execute("SELECT id_carc FROM carcerato WHERE locType != 'Cella' AND locType IS NOT NULL")
        carcerati_ids = [row[0] for row in self.__cur.fetchall()]
        if not carcerati_ids:
            return
        try:
            for carc_id in carcerati_ids:
                id_cella_disponibile = self.trova_cella_disponibile()
                if id_cella_disponibile:
                    self.__cur.execute("UPDATE carcerato SET locType = 'Cella', locId = %s WHERE id_carc = %s",
                                       (id_cella_disponibile, carc_id))
            self.__con.commit()
            self.ottieni_carcerati()
        except sql.Error as err:
            print(f"Errore durante il riporto nelle celle: {err}")

    def controlla_e_distribuisci(self):
        ora_corrente = datetime.now()
        ora = ora_corrente.hour
        minuto = ora_corrente.minute
        
        if ora == 12 and minuto == 0:
            self.distribuisci_carcerati_nelle_mense()
        else:
            if ora == 16 and minuto == 0:
                self.distribuisci_carcerati_nei_cortili()
            else:
                self.riporta_carcerati_nelle_celle()
        
        self.after(60000, self.controlla_e_distribuisci)


    def crea_combobox_localita(self):
        self.__etichetta_tipo_localita = tk.Label(self, text="Seleziona tipo di località:")
        self.__combobox_tipo_localita = ttk.Combobox(self) 
        self.__combobox_tipo_localita.bind('<<ComboboxSelected>>', self.su_selezione_tipo_localita)

        self.__etichetta_localita = tk.Label(self, text="Seleziona località:")
        self.__combobox_localita = ttk.Combobox(self)
        self.__combobox_localita.bind('<<ComboboxSelected>>', self.su_selezione_localita)
    
    def popola_combobox_localita(self, tipo_localita):
        self.__tipo_localita_selezionata = tipo_localita
        tipo_map = {"Cella": list(self.__sezioni.keys()), "Cortile": self.__cortili, "Mensa": self.__mense}
        self.__combobox_localita['values'] = tipo_map.get(tipo_localita, [])

    def popola_combobox(self, combobox, values):
        combobox['values'] = values
        if values:
            combobox.set(values[0])

    def popola_combobox_carcerati_gestione(self):
        self.popola_combobox(self.__combobox_rimuovi_carcerato_id, self.ottieni_carcerati())

    def popola_combobox_personale_gestione(self):
        self.popola_combobox(self.__combobox_rimuovi_personale_id, self.ottieni_personale())

    def su_selezione_tipo_localita(self, event):
        selected_type = self.__combobox_tipo_localita.get()
        self.popola_combobox_localita(selected_type)
        if self.__combobox_localita['values']:
            self.__combobox_localita.set(self.__combobox_localita['values'][0])
            self.su_selezione_localita(None)
        else:
            self.__combobox_localita.set("")
            self.aggiorna_lista_carcerati([])

    def estrai_id(self, text):
        return text.split(' -')[0] if ' -' in text else text

    def su_selezione_localita(self, event):
        selected_localita_full = self.__combobox_localita.get()
        if not selected_localita_full:
            self.aggiorna_lista_carcerati([])
            return
        self.__id_localita_selezionata = self.estrai_id(selected_localita_full)
        self.aggiorna_lista_carcerati(self.ottieni_carcerati(
            tipo_localita=self.__tipo_localita_selezionata.lower(),
            id_localita=self.__id_localita_selezionata
        ))

    def aggiorna_lista_carcerati(self, carcerati):
        self.__lista_carcerati.delete(0, tk.END)
        self.__lista_carcerati.insert(0, *carcerati)

    def su_selezione_carcerato(self, event):
        selected_index = self.__lista_carcerati.curselection()
        if selected_index:
            id_carcerato = self.estrai_id(self.__lista_carcerati.get(selected_index[0]))
            self.mostra_dettagli_carcerato(id_carcerato)

    def aggiorna_campo_entry(self, campo, valore):
        campo.delete(0, tk.END)
        campo.insert(0, valore)

    def mostra_dettagli_carcerato(self, id_carcerato):
        self.__id_carcerato_corrente = id_carcerato
        dati = self.ottieni_dati_carcerato(id_carcerato)
        self.__campi["ID Carcerato"].config(text=id_carcerato)
        self.aggiorna_campo_entry(self.__campi["Nome"], dati.get('nome', ''))
        self.aggiorna_campo_entry(self.__campi["Cognome"], dati.get('cognome', ''))
        self.__campi["Località Corrente"].config(text=dati.get('tipo_localita_corrente', ''))
        self.__campi["ID Località Corrente"].config(text=dati.get('id_localita_corrente', ''))
        self.__casella_password.delete(0, tk.END)
        self.__cornice_dettagli_carcerato.place(x=400, y=10, width=380, height=280) 

    def valida_password(self, password_widget):
        if password_widget.get() != "00000000":
            tk.messagebox.showerror("Errore", "Password errata!")
            return False
        return True

    def salva_modifiche_carcerato(self):
        if not self.valida_password(self.__casella_password):
            return
        try:
            self.__cur.execute("UPDATE carcerato SET nome = %s, cognome = %s WHERE id_carc = %s",
                               (self.__campi["Nome"].get(), self.__campi["Cognome"].get(), self.__id_carcerato_corrente))
            self.__con.commit()
            tk.messagebox.showinfo("Successo", "Dati carcerato aggiornati!")
            self.ottieni_carcerati()
            self.aggiorna_lista_carcerati(self.ottieni_carcerati(
                tipo_localita=self.__tipo_localita_selezionata.lower(),
                id_localita=self.__id_localita_selezionata
            ))
            self.__cornice_dettagli_carcerato.place_forget()
        except sql.Error as err:
            tk.messagebox.showerror("Errore Database", f"Errore: {err}")

    def annulla_modifiche_carcerato(self):
        self.__casella_password.delete(0, tk.END)
        self.__cornice_dettagli_carcerato.place_forget()

    def su_selezione_personale(self, event):
        selected_index = self.__combobox_personale.get()
        if selected_index:
            self.mostra_dettagli_personale(self.estrai_id(selected_index))

    def mostra_dettagli_personale(self, id_personale):
        self.__id_personale_corrente = id_personale
        dati = self.ottieni_dati_personale(id_personale)
        self.__campi_pers["ID Personale"].config(text=id_personale)
        self.aggiorna_campo_entry(self.__campi_pers["Nome"], dati.get('nome', ''))
        self.aggiorna_campo_entry(self.__campi_pers["Cognome"], dati.get('cognome', ''))
        self.__campi_pers["Ruolo"].config(text=dati.get('ruolo', ''))
        self.__campi_pers["Dotazione"].config(text=dati.get('dotazione', ''))
        self.__cornice_dettagli_personale.place(x=400, y=10, width=380, height=280) 

    def salva_modifiche_personale(self):
        if not self.valida_password(self.__casella_password_pers):
            return
        try:
            nome, cognome = self.__campi_pers["Nome"].get(), self.__campi_pers["Cognome"].get()
            self.__cur.execute("UPDATE personale SET nome = %s, cognome = %s WHERE id_pers = %s",
                               (nome, cognome, self.__id_personale_corrente))
            self.__con.commit()
            tk.messagebox.showinfo("Successo", "Dati personale aggiornati!")
            personale_values = self.ottieni_personale()
            self.__combobox_personale['values'] = personale_values
            self.__combobox_personale.set(f"{self.__id_personale_corrente} - {nome} {cognome} ({self.__campi_pers['Ruolo'].cget('text')})")
            self.__cornice_dettagli_personale.place_forget()
            self.__casella_password_pers.delete(0, tk.END)
        except sql.Error as err:
            tk.messagebox.showerror("Errore Database", f"Errore: {err}")

    def annulla_modifiche_personale(self):
        self.__casella_password_pers.delete(0, tk.END)
        self.__cornice_dettagli_personale.place_forget()

    def trova_nome_localita(self, tipo, id_localita):
        tipo_map = {
            "Cella": id_localita if id_localita else "Default Cella",
            "Cortile": next((c for c in self.__cortili if c.startswith(f"{id_localita} -")), ""),
            "Mensa": next((m for m in self.__mense if m.startswith(f"{id_localita} -")), "")
        }
        return tipo_map.get(tipo, "")

    def cerca_carcerato(self):
        try:
            id_carcerato = int(self.__casella_ricerca.get())
            self.__cur.execute("SELECT locType, locId FROM carcerato WHERE id_carc = %s", (id_carcerato,))
            result = self.__cur.fetchone()
            if not result:
                tk.messagebox.showerror("Errore", f"Carcerato con ID {id_carcerato} non trovato.")
                return
            tipo, id_loc = result
            if tipo and (id_loc or tipo == "Cella"):
                self.__combobox_tipo_localita.set(tipo)
                self.popola_combobox_localita(tipo)
                full_name = self.trova_nome_localita(tipo, id_loc)
                if full_name:
                    self.__combobox_localita.set(full_name)
                    self.su_selezione_localita(None)
                    self.seleziona_carcerato_in_lista(id_carcerato)
                    return
            tk.messagebox.showinfo("Ricerca Carcerato", f"Carcerato con ID {id_carcerato} trovato, ma la sua località corrente non è definita o non valida.")
            self.mostra_dettagli_carcerato(id_carcerato)
        except ValueError:
            tk.messagebox.showerror("Errore", "Per favorire, inserisci un ID carcerato numerico.")

    def seleziona_carcerato_in_lista(self, id_carcerato):
        self.__lista_carcerati.selection_clear(0, tk.END)
        for i in range(self.__lista_carcerati.size()):
            if self.__lista_carcerati.get(i).startswith(f"{id_carcerato} -"):
                self.__lista_carcerati.selection_set(i)
                self.__lista_carcerati.see(i)
                self.mostra_dettagli_carcerato(id_carcerato)
                break
        
    def aggiorna(self):
        self.__tempo=datetime.now().strftime("%H:%M:%S")
        self.__ora.config(text=self.__tempo)

    def trova_cella_disponibile(self):
        for cell_id, capienza in self.__sezioni.items():
            self.__cur.execute("SELECT COUNT(*) FROM carcerato WHERE locType = 'Cella' AND locId = %s", (cell_id,))
            if self.__cur.fetchone()[0] < capienza:
                return cell_id
        return None

    def pulisci_campi_entry(self, *widgets):
        for widget in widgets:
            widget.delete(0, tk.END)

    def aggiungi_carcerato(self):
        campi = [self.__entry_carcerato_nome.get(), self.__entry_carcerato_cognome.get(), 
                 self.__entry_carcerato_data_nascita.get(), self.__combobox_carcerato_nazionalita.get(),
                 self.__entry_carcerato_pena.get(), self.__entry_carcerato_reato.get()]
        if not all(campi):
            tk.messagebox.showerror("Errore", "Tutti i campi del carcerato devono essere compilati!")
            return
        try:
            nome, cognome, data_nascita_str, nazionalita, pena, reato = campi
            data_nascita = datetime.strptime(data_nascita_str, "%Y-%m-%d").date()
            cf = f"{nome[:3].upper()}{cognome[:3].upper()}{data_nascita.year}"
            id_cella = self.trova_cella_disponibile()
            if not id_cella:
                tk.messagebox.showwarning("Attenzione", "Nessuna cella disponibile. Il carcerato verrà aggiunto senza assegnazione immediata a una cella.")
                loc_type, loc_id = None, None
            else:
                loc_type, loc_id = 'Cella', id_cella
            self.__cur.execute("INSERT INTO carcerato (cf, nome, cognome, data_nascita, nazionalita, pena, reato, locType, locId) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                               (cf, nome, cognome, data_nascita, nazionalita, pena, reato, loc_type, loc_id))
            self.__con.commit()
            tk.messagebox.showinfo("Successo", "Carcerato aggiunto con successo!")
            self.ottieni_carcerati()
            self.popola_combobox_carcerati_gestione()
            self.pulisci_campi_entry(self.__entry_carcerato_nome, self.__entry_carcerato_cognome, 
                                      self.__entry_carcerato_data_nascita, self.__entry_carcerato_pena, 
                                      self.__entry_carcerato_reato)
            self.__combobox_carcerato_nazionalita.set('')
        except ValueError:
            tk.messagebox.showerror("Errore", "Formato data di nascita non valido. Usa YYYY-MM-DD")
        except sql.Error as err:
            tk.messagebox.showerror("Errore Database", f"Errore nell'aggiungere carcerato: {err}")

    def rimuovi_carcerato(self):
        selected = self.__combobox_rimuovi_carcerato_id.get()
        if not selected:
            tk.messagebox.showerror("Errore", "Seleziona un carcerato da rimuovere.")
            return
        id_carcerato = self.estrai_id(selected)
        if not tk.messagebox.askyesno("Conferma Rimozione", f"Sei sicuro di voler rimuovere il carcerato con ID {id_carcerato}? Organizza i dati con cura in modo da non incappare in errori"):
            return
        try:
            self.__cur.execute("DELETE FROM visita_medica WHERE id_carc = %s", (id_carcerato,))
            self.__cur.execute("DELETE FROM carcerato WHERE id_carc = %s", (id_carcerato,))
            self.__con.commit()
            tk.messagebox.showinfo("Successo", "Carcerato rimosso con successo!")
            self.ottieni_carcerati()
            self.popola_combobox_carcerati_gestione()
            self.su_selezione_localita(None)
        except sql.Error as err:
            tk.messagebox.showerror("Errore Database", f"Errore nel rimuovere carcerato: {err}")

    def aggiungi_turno(self):
        id_personale = self.estrai_id(self.__combobox_turno_personale_id.get())
        inizio_str, fine_str = self.__entry_turno_inizio.get(), self.__entry_turno_fine.get()
        if not all([id_personale, inizio_str, fine_str]):
            tk.messagebox.showerror("Errore", "Tutti i campi del turno devono essere compilati!")
            return
        try:
            today = datetime.now().date()
            inizio = datetime.combine(today, datetime.strptime(inizio_str, "%H:%M").time())
            fine = datetime.combine(today, datetime.strptime(fine_str, "%H:%M").time())
            if inizio >= fine:
                tk.messagebox.showerror("Errore", "L'ora di inizio turno deve essere precedente all'ora di fine turno.")
                return
            self.__cur.execute("INSERT INTO turno (id_pers, inizio, fine) VALUES (%s, %s, %s)",
                               (int(id_personale), inizio, fine))
            self.__con.commit()
            tk.messagebox.showinfo("Successo", "Turno aggiunto con successo!")
            self.aggiorna_lista_turni()
            self.pulisci_campi_entry(self.__entry_turno_inizio, self.__entry_turno_fine)
        except ValueError:
            tk.messagebox.showerror("Errore", "Formato ora non valido. Usa HH:MM (es. 08:00)")
        except sql.Error as err:
            tk.messagebox.showerror("Errore Database", f"Errore nell'aggiungere turno: {err}")

    def aggiungi_personale(self):
        campi = [self.__entry_personale_nome.get(), self.__entry_personale_cognome.get(),
                 self.__entry_personale_data_nascita.get(), self.__combobox_personale_ruolo.get(),
                 self.__entry_personale_dotazione.get()]
        if not all(campi):
            tk.messagebox.showerror("Errore", "Tutti i campi del personale devono essere compilati!")
            return
        try:
            nome, cognome, data_nascita_str, ruolo, dotazione_str = campi
            data_nascita = datetime.strptime(data_nascita_str, "%Y-%m-%d").date()
            cf = f"{nome[:3].upper()}{cognome[:3].upper()}{data_nascita.year}P"
            self.__cur.execute("INSERT INTO personale (cf, nome, cognome, data_nascita, ruolo, dotazione) VALUES (%s, %s, %s, %s, %s, %s)",
                               (cf, nome, cognome, data_nascita, ruolo, int(dotazione_str)))
            self.__con.commit()
            tk.messagebox.showinfo("Successo", "Personale aggiunto con successo!")
            personale_values = self.ottieni_personale()
            self.popola_combobox_personale_gestione()
            self.__combobox_turno_personale_id['values'] = personale_values
            self.__combobox_personale['values'] = personale_values
            self.pulisci_campi_entry(self.__entry_personale_nome, self.__entry_personale_cognome,
                                      self.__entry_personale_data_nascita, self.__entry_personale_dotazione)
            self.__combobox_personale_ruolo.set('')
        except ValueError:
            tk.messagebox.showerror("Errore", "Formato data di nascita o dotazione non valido. Usa YYYY-MM-DD per la data e un numero per la dotazione.")
        except sql.Error as err:
            tk.messagebox.showerror("Errore Database", f"Errore nell'aggiungere personale: {err}")

    def rimuovi_personale(self):
        selected = self.__combobox_rimuovi_personale_id.get()
        if not selected:
            tk.messagebox.showerror("Errore", "Seleziona un membro del personale da rimuovere.")
            return
        id_personale = self.estrai_id(selected)
        if not tk.messagebox.askyesno("Conferma Rimozione", f"Sei sicuro di voler rimuovere il personale con ID {id_personale}? Organizza i dati con cura in modo da non incappare in errori"):
            return
        try:
            self.__cur.execute("DELETE FROM turno WHERE id_pers = %s", (id_personale,))
            self.__cur.execute("UPDATE visita_medica SET id_medico = NULL WHERE id_medico = %s", (id_personale,))
            self.__cur.execute("DELETE FROM personale WHERE id_pers = %s", (id_personale,))
            self.__con.commit()
            tk.messagebox.showinfo("Successo", "Personale rimosso con successo!")
            personale_values = self.ottieni_personale()
            self.popola_combobox_personale_gestione()
            self.__combobox_turno_personale_id['values'] = personale_values
            self.__combobox_personale['values'] = personale_values
            self.aggiorna_lista_turni()
        except sql.Error as err:
            tk.messagebox.showerror("Errore Database", f"Errore nel rimuovere personale: {err}")

    def aggiorna_lista_turni(self):
        self.__lista_turni.delete(0, tk.END)
        turni = self.ottieni_turni()
        now = datetime.now()
        if turni:
            upcoming_shifts = sorted([t for t in turni if t[3] > now], key=lambda x: x[3])
            if upcoming_shifts:
                next_shift = upcoming_shifts[0]
                self.__etichetta_turni_personale.config(text=f"Prossimo Turno Personale: {next_shift[1]} {next_shift[2]} dalle {next_shift[3].strftime('%H:%M')} alle {next_shift[4].strftime('%H:%M')}")
            else:
                self.__etichetta_turni_personale.config(text="Turni Personale: Nessun turno futuro")
            current_shifts = [t for t in turni if t[3] <= now <= t[4]]
            if current_shifts:
                current_personnel = ", ".join([f"{s[1]} {s[2]}" for s in current_shifts])
                self.__etichetta_turno_personale_attuale.config(text=f"Attualmente di turno: {current_personnel}")
            else:
                self.__etichetta_turno_personale_attuale.config(text="Attualmente di turno: Nessuno")
            for turno in turni:
                self.__lista_turni.insert(tk.END, f"ID Turno: {turno[0]}, Personale: {turno[1]} {turno[2]}, Inizio: {turno[3].strftime('%H:%M')}, Fine: {turno[4].strftime('%H:%M')}")
        else:
            self.__etichetta_turni_personale.config(text="Turni Personale: Nessun turno registrato")
            self.__etichetta_turno_personale_attuale.config(text="Attualmente di turno: Nessuno")

    def inizializza_dati_e_ui(self):
        self.__combobox_tipo_localita['values'] = ["Cella", "Cortile", "Mensa"]
        self.__combobox_tipo_localita.set(self.__combobox_tipo_localita['values'][0])
        self.popola_combobox_localita(self.__combobox_tipo_localita.get())
        if self.__combobox_localita['values']:
            self.__combobox_localita.set(self.__combobox_localita['values'][0])
            self.su_selezione_localita(None)
        personale_values = self.ottieni_personale()
        self.popola_combobox(self.__combobox_personale, personale_values)
        self.popola_combobox(self.__combobox_turno_personale_id, personale_values)
        self.aggiorna_lista_turni()
        self.popola_combobox_carcerati_gestione()
        self.popola_combobox_personale_gestione()

    def creaWidget(self):
        self.__ora=tk.Label(self, text=self.__tempo)
        self.__aggiorna=tk.Button(self, text="Aggiorna",command=self.aggiorna)
        # Crea il frame per la gestione dei carcerati
        self.__cornice_gestione_carcerati = tk.LabelFrame(self, text="Gestione Carcerati", padx=10, pady=10)
        self.__etichetta_carcerato_nome = tk.Label(self.__cornice_gestione_carcerati, text="Nome:")
        self.__entry_carcerato_nome = tk.Entry(self.__cornice_gestione_carcerati)
        self.__etichetta_carcerato_cognome = tk.Label(self.__cornice_gestione_carcerati, text="Cognome:")
        self.__entry_carcerato_cognome = tk.Entry(self.__cornice_gestione_carcerati)
        self.__etichetta_carcerato_data_nascita = tk.Label(self.__cornice_gestione_carcerati, text="Data Nascita (YYYY-MM-DD):")
        self.__entry_carcerato_data_nascita = tk.Entry(self.__cornice_gestione_carcerati)
        self.__etichetta_carcerato_nazionalita = tk.Label(self.__cornice_gestione_carcerati, text="Nazionalità:")
        self.__combobox_carcerato_nazionalita = ttk.Combobox(self.__cornice_gestione_carcerati, values=['Italiana','Rumena','Albanese','Marocchina','Senegalese','Nigeriana','Cinese','Indiana','Giappone','Statunitense','Brasiliana','Messicana'])
        self.__etichetta_carcerato_pena = tk.Label(self.__cornice_gestione_carcerati, text="Pena:")
        self.__entry_carcerato_pena = tk.Entry(self.__cornice_gestione_carcerati)
        self.__etichetta_carcerato_reato = tk.Label(self.__cornice_gestione_carcerati, text="Reato:")
        self.__entry_carcerato_reato = tk.Entry(self.__cornice_gestione_carcerati)
        self.__pulsante_aggiungi_carcerato = tk.Button(self.__cornice_gestione_carcerati, text="Aggiungi Carcerato", command=self.aggiungi_carcerato)
        self.__etichetta_rimuovi_carcerato = tk.Label(self.__cornice_gestione_carcerati, text="Rimuovi Carcerato (ID):")
        self.__combobox_rimuovi_carcerato_id = ttk.Combobox(self.__cornice_gestione_carcerati)
        self.__pulsante_rimuovi_carcerato = tk.Button(self.__cornice_gestione_carcerati, text="Rimuovi Carcerato", command=self.rimuovi_carcerato)
        
        # Crea il frame per la gestione del personale
        self.__cornice_gestione_personale = tk.LabelFrame(self, text="Gestione Personale", padx=10, pady=10)
        self.__etichetta_personale_nome = tk.Label(self.__cornice_gestione_personale, text="Nome:")
        self.__entry_personale_nome = tk.Entry(self.__cornice_gestione_personale)
        self.__etichetta_personale_cognome = tk.Label(self.__cornice_gestione_personale, text="Cognome:")
        self.__entry_personale_cognome = tk.Entry(self.__cornice_gestione_personale)
        self.__etichetta_personale_data_nascita = tk.Label(self.__cornice_gestione_personale, text="Data Nascita (YYYY-MM-DD):")
        self.__entry_personale_data_nascita = tk.Entry(self.__cornice_gestione_personale)
        self.__etichetta_personale_ruolo = tk.Label(self.__cornice_gestione_personale, text="Ruolo:")
        self.__combobox_personale_ruolo = ttk.Combobox(self.__cornice_gestione_personale, values=['Direttore','Secondino','Guardia','Cuoco','Medico','Educatore','Psicologo','Amministrativo'])
        self.__etichetta_personale_dotazione = tk.Label(self.__cornice_gestione_personale, text="Dotazione:")
        self.__entry_personale_dotazione = tk.Entry(self.__cornice_gestione_personale)
        self.__pulsante_aggiungi_personale = tk.Button(self.__cornice_gestione_personale, text="Aggiungi Personale", command=self.aggiungi_personale)
        self.__etichetta_rimuovi_personale = tk.Label(self.__cornice_gestione_personale, text="Rimuovi Personale (ID):")
        self.__combobox_rimuovi_personale_id = ttk.Combobox(self.__cornice_gestione_personale)
        self.__pulsante_rimuovi_personale = tk.Button(self.__cornice_gestione_personale, text="Rimuovi Personale", command=self.rimuovi_personale)
        # Inizializza la lista dei carcerati e la sua etichetta
        self.__etichetta_lista_carcerati = tk.Label(self, text="Carcerati nella località selezionata:")
        self.__lista_carcerati = tk.Listbox(self)
        self.__lista_carcerati.bind('<<ListboxSelect>>', self.su_selezione_carcerato)

        self.crea_combobox_localita()

        # Crea la combobox del personale
        self.__etichetta_personale = tk.Label(self, text="Seleziona Personale:")
        self.__combobox_personale = ttk.Combobox(self)
        self.__combobox_personale.bind('<<ComboboxSelected>>', self.su_selezione_personale)

        # Crea il frame per i dettagli del personale e i suoi widget
        self.__cornice_dettagli_personale = tk.LabelFrame(self, text="Dettagli Personale", padx=10, pady=10)
        self.__campi_pers = {}
        fields_pers = ["ID Personale", "Nome", "Cognome", "Ruolo", "Dotazione"]
        for i, field in enumerate(fields_pers):
            tk.Label(self.__cornice_dettagli_personale, text=f"{field}:").grid(row=i, column=0, sticky="w", pady=2)
            if field in ["ID Personale", "Ruolo", "Dotazione"]:
                valore_etichetta = tk.Label(self.__cornice_dettagli_personale, text="")
                valore_etichetta.grid(row=i, column=1, sticky="ew", pady=2)
                self.__campi_pers[field] = valore_etichetta
            else:
                campo = tk.Entry(self.__cornice_dettagli_personale)
                campo.grid(row=i, column=1, sticky="ew", pady=2)
                self.__campi_pers[field] = campo
        
        self.__pulsante_salva_pers = tk.Button(self.__cornice_dettagli_personale, text="Salva Modifiche", command=self.salva_modifiche_personale)
        self.__pulsante_salva_pers.grid(row=len(fields_pers) + 1, column=0, pady=5)
        self.__pulsante_annulla_pers = tk.Button(self.__cornice_dettagli_personale, text="Annulla", command=self.annulla_modifiche_personale)
        self.__pulsante_annulla_pers.grid(row=len(fields_pers) + 1, column=1, pady=5)

        self.__etichetta_password_pers = tk.Label(self.__cornice_dettagli_personale, text="Password per modificare:")
        self.__etichetta_password_pers.grid(row=len(fields_pers) + 2, column=0, sticky="w", pady=2)
        self.__casella_password_pers = tk.Entry(self.__cornice_dettagli_personale, show="*")
        self.__casella_password_pers.grid(row=len(fields_pers) + 2, column=1, sticky="ew", pady=2)

        # Crea il frame per la gestione dei turni del personale
        self.__cornice_gestione_turni = tk.LabelFrame(self, text="Gestione Turni Personale", padx=10, pady=10)
        self.__etichetta_turno_personale_id = tk.Label(self.__cornice_gestione_turni, text="ID Personale:")
        self.__etichetta_turno_personale_id.grid(row=0, column=0, sticky="w", pady=2)
        self.__combobox_turno_personale_id = ttk.Combobox(self.__cornice_gestione_turni)
        self.__combobox_turno_personale_id.grid(row=0, column=1, sticky="ew", pady=2)

        self.__etichetta_turno_inizio = tk.Label(self.__cornice_gestione_turni, text="Inizio (HH:MM):")
        self.__etichetta_turno_inizio.grid(row=1, column=0, sticky="w", pady=2)
        self.__entry_turno_inizio = tk.Entry(self.__cornice_gestione_turni)
        self.__entry_turno_inizio.grid(row=1, column=1, sticky="ew", pady=2)

        self.__etichetta_turno_fine = tk.Label(self.__cornice_gestione_turni, text="Fine (HH:MM):")
        self.__etichetta_turno_fine.grid(row=2, column=0, sticky="w", pady=2)
        self.__entry_turno_fine = tk.Entry(self.__cornice_gestione_turni)
        self.__entry_turno_fine.grid(row=2, column=1, sticky="ew", pady=2)

        self.__pulsante_aggiungi_turno = tk.Button(self.__cornice_gestione_turni, text="Aggiungi Turno", command=self.aggiungi_turno)
        self.__pulsante_aggiungi_turno.grid(row=3, column=0, columnspan=2, pady=5)

        # Visualizza i turni esistenti
        self.__etichetta_lista_turni = tk.Label(self.__cornice_gestione_turni, text="Turni Esistenti:")
        self.__etichetta_lista_turni.grid(row=4, column=0, sticky="w", pady=2)
        self.__lista_turni = tk.Listbox(self.__cornice_gestione_turni, height=8, width=60)
        self.__lista_turni.grid(row=5, column=0, columnspan=2, sticky="ew", pady=2, padx=2)

        # Etichetta per il personale attualmente di turno
        self.__etichetta_turno_personale_attuale = tk.Label(self.__cornice_gestione_turni, text="Attualmente di turno: Nessuno")
        self.__etichetta_turno_personale_attuale.grid(row=6, column=0, columnspan=2, sticky="w", pady=2)

        # Crea i widget della barra di ricerca
        self.__etichetta_ricerca = tk.Label(self, text="Cerca Carcerato (ID):")
        self.__casella_ricerca = tk.Entry(self)
        self.__pulsante_ricerca = tk.Button(self, text="Cerca", command=self.cerca_carcerato)

        # Crea il frame per i dettagli del carcerato e i suoi widget
        self.__cornice_dettagli_carcerato = tk.LabelFrame(self, text="Dettagli Carcerato", padx=10, pady=10)
        self.__campi = {}
        fields = ["ID Carcerato", "Nome", "Cognome", "Località Corrente", "ID Località Corrente"]
        for i, field in enumerate(fields):
            tk.Label(self.__cornice_dettagli_carcerato, text=f"{field}:").grid(row=i, column=0, sticky="w", pady=2)
            if field in ["ID Carcerato", "Località Corrente", "ID Località Corrente"]:
                valore_etichetta = tk.Label(self.__cornice_dettagli_carcerato, text="")
                valore_etichetta.grid(row=i, column=1, sticky="ew", pady=2)
                self.__campi[field] = valore_etichetta
            else:
                campo = tk.Entry(self.__cornice_dettagli_carcerato)
                campo.grid(row=i, column=1, sticky="ew", pady=2)
                self.__campi[field] = campo
        
        self.__etichetta_password = tk.Label(self.__cornice_dettagli_carcerato, text="Password per modificare:")
        self.__etichetta_password.grid(row=len(fields), column=0, sticky="w", pady=2)
        self.__casella_password = tk.Entry(self.__cornice_dettagli_carcerato, show="*")
        self.__casella_password.grid(row=len(fields), column=1, sticky="ew", pady=2)

        self.__pulsante_salva = tk.Button(self.__cornice_dettagli_carcerato, text="Salva Modifiche", command=self.salva_modifiche_carcerato)
        self.__pulsante_salva.grid(row=len(fields) + 1, column=0, pady=5)
        self.__pulsante_annulla = tk.Button(self.__cornice_dettagli_carcerato, text="Annulla", command=self.annulla_modifiche_carcerato)
        self.__pulsante_annulla.grid(row=len(fields) + 1, column=1, pady=5)
        
    def lM(self):
        self.__ora.place(x=10,y=10)
        self.__aggiorna.place(x=10,y=30)

        self.__etichetta_tipo_localita.place(x=10, y=60)
        self.__combobox_tipo_localita.place(x=150, y=60)

        self.__etichetta_localita.place(x=10, y=90)
        self.__combobox_localita.place(x=150, y=90)

        self.__etichetta_lista_carcerati.place(x=10, y=120)
        self.__lista_carcerati.place(x=10, y=150, width=300, height=200)
        self.__etichetta_ricerca.place(x=10, y=360)
        self.__casella_ricerca.place(x=150, y=360)
        self.__pulsante_ricerca.place(x=280, y=360)
        self.__etichetta_personale.place(x=10, y=420)
        self.__combobox_personale.place(x=150, y=420)

        # Etichetta stato turni personale
        self.__etichetta_turni_personale = tk.Label(self, text="Turni Personale: Nessun turno attivo")
        self.__etichetta_turni_personale.place(x=10, y=450)
        self.__cornice_dettagli_carcerato.place_forget()
        self.__cornice_dettagli_personale.place_forget()
        self.__cornice_gestione_turni.place(x=800, y=10, width=380, height=280) 
        self.__cornice_gestione_carcerati.place(x=400, y=300, width=380, height=380)
        self.__cornice_gestione_personale.place(x=400, y=590, width=380, height=380)

        self.__etichetta_personale_nome.grid(row=0, column=0, sticky="w", pady=2)
        self.__entry_personale_nome.grid(row=0, column=1, sticky="ew", pady=2)
        self.__etichetta_personale_cognome.grid(row=1, column=0, sticky="w", pady=2)
        self.__entry_personale_cognome.grid(row=1, column=1, sticky="ew", pady=2)
        self.__etichetta_personale_data_nascita.grid(row=2, column=0, sticky="w", pady=2)
        self.__entry_personale_data_nascita.grid(row=2, column=1, sticky="ew", pady=2)
        self.__etichetta_personale_ruolo.grid(row=3, column=0, sticky="w", pady=2)
        self.__combobox_personale_ruolo.grid(row=3, column=1, sticky="ew", pady=2)
        self.__etichetta_personale_dotazione.grid(row=4, column=0, sticky="w", pady=2)
        self.__entry_personale_dotazione.grid(row=4, column=1, sticky="ew", pady=2)
        self.__pulsante_aggiungi_personale.grid(row=5, column=0, columnspan=2, pady=5)
        self.__etichetta_rimuovi_personale.grid(row=6, column=0, sticky="w", pady=2)
        self.__combobox_rimuovi_personale_id.grid(row=6, column=1, sticky="ew", pady=2)
        self.__pulsante_rimuovi_personale.grid(row=7, column=0, columnspan=2, pady=5)

        self.__etichetta_carcerato_nome.grid(row=0, column=0, sticky="w", pady=2)
        self.__entry_carcerato_nome.grid(row=0, column=1, sticky="ew", pady=2)
        self.__etichetta_carcerato_cognome.grid(row=1, column=0, sticky="w", pady=2)
        self.__entry_carcerato_cognome.grid(row=1, column=1, sticky="ew", pady=2)
        self.__etichetta_carcerato_data_nascita.grid(row=2, column=0, sticky="w", pady=2)
        self.__entry_carcerato_data_nascita.grid(row=2, column=1, sticky="ew", pady=2)
        self.__etichetta_carcerato_nazionalita.grid(row=3, column=0, sticky="w", pady=2)
        self.__combobox_carcerato_nazionalita.grid(row=3, column=1, sticky="ew", pady=2)
        self.__etichetta_carcerato_pena.grid(row=4, column=0, sticky="w", pady=2)
        self.__entry_carcerato_pena.grid(row=4, column=1, sticky="ew", pady=2)
        self.__etichetta_carcerato_reato.grid(row=5, column=0, sticky="w", pady=2)
        self.__entry_carcerato_reato.grid(row=5, column=1, sticky="ew", pady=2)
        self.__pulsante_aggiungi_carcerato.grid(row=6, column=0, columnspan=2, pady=5)
        self.__etichetta_rimuovi_carcerato.grid(row=7, column=0, sticky="w", pady=2)
        self.__combobox_rimuovi_carcerato_id.grid(row=7, column=1, sticky="ew", pady=2)
        self.__pulsante_rimuovi_carcerato.grid(row=8, column=0, columnspan=2, pady=5)

p=Penitenziario()
