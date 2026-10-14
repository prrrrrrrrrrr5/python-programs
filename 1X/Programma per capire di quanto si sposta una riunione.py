print("Questo programma serve per calcolare a quando viene rimandata una riunione")

OrarioRiunione=float(input("Scrivi a che orario era programmata la riunione "))

OreRinvio=float(input("Bene, ora scrivi di quante ore è stata rimandata la riunione "))

Giorno=float(input("Infine scrivi che giorno è oggi, "))
Mese=float(input("Quanti giorni ha il mese corrente, "))
MeseNome=input("Ora anche il nome del mese (se sai che la riunione avverrà nel prossimo mese allora digita il nome del prossimo mese) ")
Anno=input("E anche l'anno corrente ")

A=((OreRinvio%24)+OrarioRiunione)%24
B=OreRinvio//24

print("Bene, la tua riunione è stata rimandata al" ,(Giorno+B)%Mese,)
print(MeseNome)
print(Anno)
print("Alle ore:" ,A,)
