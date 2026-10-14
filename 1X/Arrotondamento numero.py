print("Questo programma serve per arrotondare un numero per eccesso o per difetto ad una cifra decimale da te scelta")

Numero=float(input("Inserisci il numero da te scelto "))
Decimale=str(input("Ora inserisci la cifra decimale da te scelta (Numero intero, decimi, centesimi, millesimi) "))
Decimale1= ("millesimi")
Decimale2= ("centesimi")
Decimale3= ("decimi")
Decimale4= ("numero intero")
if Decimale==Decimale4:
    Resto=Numero%1
    if Resto<= .4:
        print("Il numero arrotondato è" ,Numero-Resto,)
    elif Resto>= .5:
        print("Il numero arrotondato è" ,(Numero-Resto)+1,)
elif Decimale==Decimale3:
    Resto2=Numero%0.1
    if Resto2<= .04:
        print("Il numero arrotondato è" ,Numero-Resto2,)
    elif Resto2>= .05:
        print("Il numero arrotondato è" ,(Numero-Resto2)+0.1)
elif Decimale==Decimale2:
    Resto3=Numero%0.01
    if Resto3<= .004:
        print("Il numero arrotondato è" ,Numero-Resto3,)
    elif Resto3>= .005:
        print("Il numero arrotondato è" ,(Numero-Resto3)+0.01)
elif Decimale==Decimale1:
    Resto3=Numero%0.001
    if Resto3<= .0004:
        print("Il numero arrotondato è" ,Numero-Resto3,)
    elif Resto3>= .0005:
        print("Il numero arrotondato è" ,(Numero-Resto3)+0.001)
