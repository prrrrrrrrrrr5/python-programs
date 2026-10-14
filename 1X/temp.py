#<<Noto il numero totale di secondi corrispondenti al tempo registrato da un maratoneta in una gara, esprimere tale tempo in ore, minuti e secondi e mostrarlo in output.>>

SecondiMaratoneta=int(input("Inserisci di seguito i secondi impiegati da un maratoneta per finire una maratona \n --> "))
NOre=SecondiMaratoneta//60
RestoOre=SecondiMaratoneta%60
NMinuti=RestoOre//60
RestoMinuti=RestoOre%60
NSecondi=RestoMinuti

print("Il maratoneta ha impiegato " ,NOre, "ore, " ,NMinuti, "minuti e " ,NSecondi, "secondi")
