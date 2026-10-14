#Inizio
tVoc=0
tE=0
tO=0
voc="aeiou"
parola=input("Inserisci di seguito la parola che hai scelto \n --> ").lower()
for i in range(len(parola)):
    if parola[i] in voc:
        tVoc=tVoc+1
        if parola[i]=="e":
            tE=tE+1
        else:
            if parola[i]=="o":
                tO=tO+1
if tE>tO:
    print("Il numero di caratteri \"e\" è maggiore del numero dei caratteri \"o\"")
else:
    if tE==tO:
        print("Il numero di caratteri \"o\" è uguale del numero dei caratteri \"e\"")
    else:
        print("Il numero di caratteri \"o\" è maggiore del numero dei caratteri \"e\"")
    #Fine se
#Fine se

print("Il numero delle vocali è" ,tVoc,)

#Fine
