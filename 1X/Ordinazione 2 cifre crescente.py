print("Questo programma serve per ordinare 2 cifre inserite dall'utente in ordine crescente")

Cifra1=float(input("Inserisci la prima cifra "))
Cifra2=float(input("Ora inserisci la seconda cifra "))

if Cifra1<Cifra2:
    print("Ok, la minore è" ,Cifra1, "e la maggiore" ,Cifra2,)
elif Cifra1==Cifra2:
    print("Le due cifre sono uguali e sono" ,Cifra1,Cifra2,)
elif Cifra2<Cifra1:
    print("Ok, la cifra minore è" ,Cifra2, "e la maggiroe" ,Cifra1,)
