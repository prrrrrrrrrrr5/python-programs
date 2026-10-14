print("Questo programma serve per trasformare 4 componenti di un numero intero (migliaia, centinaia, decine e unità) in un numero intero")
Migliaia=int(input("Prima inserisci un numero appartenente alla famiglia delle migliaglia entro il 9999 "))
Centinaia=int(input("Ora inserisci un numero appartenente alla famiglia delle centinaia entro il 999 "))
Decine=int(input("Ora inserisci un numero appartenente alla famiglia delle decine entro il 99 "))
Unita=int(input("Ora inserisci un numero appartenente alla famiglia delle unità entro il  9 "))
print("Ora uscirà il numero intero")
Migliaia2=Migliaia+Centinaia//10
Centinaia2=(Centinaia%10)+(Decine//10)
Decine2=(Decine%10)+(Unita//10)
Unita2=Unita%10
print(Migliaia2,Centinaia2,Decine2,Unita2)
