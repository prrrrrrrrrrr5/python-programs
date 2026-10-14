#Inizio

def numero(n):
    lista=[1,2,1]
    lista2=lista.copy()
    print("[1] \n[1, 1] \n[1, 2, 1]")
    for i in range(n):
        lista.clear()
        lista.append(1)
        for j in range(len(lista2)-1):
            lista.append(lista2[0]+lista2[1])
            lista2.remove(lista2[0])
        #Fine per
        lista.append(1)
        lista2=lista.copy()
        print(lista)
    #Fine per

n=int(input("Quante righe deve avere il triangolo di tartaglia? \n --> "))
numero(n)

#Fine
