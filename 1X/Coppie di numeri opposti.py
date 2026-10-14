print("Questo programma serve per controllare quante coppie immesse dall'utente sono opposte")

NumeroCoppie=int(input("Inserisci quante coppie di numeri vuoi inserire di seguito --> "))
NumeriOpposti=0
for i in range(0,NumeroCoppie):
    PrimoNumeroCoppia=float(input("Inserisci il primo numero della coppia di seguito --> "))
    SecondoNumeroCoppia=float(input("Inserisci il secondo numero della coppia di seguito --> "))
    if SecondoNumeroCoppia/-1==PrimoNumeroCoppia:
        NumeriOpposti=NumeriOpposti+1
print("Le coppie con numeri opposti sono" ,NumeriOpposti,)
