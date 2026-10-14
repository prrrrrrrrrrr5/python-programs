#Inizio
tVoc=0
tE=0
tO=0
parola=input("Inserisci di seguito la parola che hai scelto \n --> ").lower()
for i in range(len(parola)):
    if parola[i]=="a":
        tVoc=tVoc+1
    else:
        if parola[i]=="e":
            tVoc=tVoc+1
            tE=tE+1
        else:
            if parola[i]=="i":
                tVoc=tVoc+1
            else:
                if parola[i]=="o":
                    tVoc=tVoc+1
                    tO=tO+1
                else:
                    if parola[i]=="u":
                        tVoc=tVoc+1
                    #Fine se
                #Fine se
            #Fine se
        #Fine se
    #Fine se
#Fine per

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
