print("Questo programma serve per mettere in ordine crescente 3 numeri")

Cifra1=float(input("Inserisci la prima cifra "))
Cifra2=float(input("Bene, ora inserisci la seconda cifra "))
Cifra3=float(input("Bene, per finire inserisci la terza cifra "))

if Cifra1<Cifra2 and Cifra1<Cifra3  and Cifra2<Cifra3:
    print("La cifra minore è" ,Cifra1, "Quella intermedia è" ,Cifra2, "e quella più grande è" ,Cifra3,)
elif Cifra2<Cifra1 and Cifra2<Cifra3 and Cifra1<Cifra3:
    print("La cifra più piccola è" ,Cifra2, "quella media è" ,Cifra1, "e la più grande è" ,Cifra3,)
elif Cifra3<Cifra1 and Cifra3<Cifra2 and Cifra1<Cifra2:
    print("La cifra più piccola è" ,Cifra3, "quella in mezzo" ,Cifra1, "Quella più grande è" ,Cifra2,)
elif Cifra1<Cifra3 and Cifra1<Cifra2 and Cifra3<Cifra2:
    print("La cifra più piccola è" ,Cifra1, "quella intermedia" ,Cifra3, "quella più grande" ,Cifra2,)
elif Cifra2<Cifra3 and Cifra2<Cifra1 and Cifra3<Cifra1:
    print("La cifra più piccola è" ,Cifra2, "quella intermedia" ,Cifra3, "quella più grande" ,Cifra1,)
elif Cifra1==Cifra2 and Cifra1<Cifra3:
    print("2 cifre sono uguali e sono:" ,Cifra1,Cifra2, "mentre la più grande è" ,Cifra3,)
elif Cifra2==Cifra3 and Cifra2<Cifra1:
    print("2 cifre sono uguali e sono" ,Cifra2,Cifra3, "e la più grande è" ,Cifra1,)
elif Cifra1==Cifra2 and Cifra3<Cifra1:
    print("La cifra più piccola è" ,Cifra3, "mentre ce ne sono 2 uguali e sono" ,Cifra1,Cifra2,)
elif Cifra2==Cifra3 and Cifra1<Cifra2:
    print("La cifra più piccola è" ,Cifra1, "mentre ce ne sono due uguali e sono" ,Cifra2,Cifra3,)
elif Cifra1==Cifra2 and Cifra2==Cifra3 and Cifra1==Cifra3:
    print("Tutte e le tre cifre sono in ordine")
    print("La cifra è" ,Cifra1,)
elif Cifra3<Cifra2 and Cifra2<Cifra1 and Cifra3<Cifra1:
    print("La cifra più piccola è" ,Cifra3, "Quella intermedia è" ,Cifra2, "quella finale è" ,Cifra1,)
