'''
<<N atleti partecipano a una gara di salto in alto, di ogni atleta è nota la 
misura raggiunta. Mostrare in output la misura del salto del vincitore.
'''

#Inizio
Natleti=int(input("Inserisci di seguito il numero di atleti che partecipano alla gara di salto \n --> "))
while Natleti<1:
    print("Dati errati")
    Natleti=int(input("Inserisca di nuovo il numero di atleti o inserisca 0 per chiudere il programma"))
    if Natleti==0:
        break
while Natleti!=0:
    Salto=float(input("Inserisci di seguito la misura del salto dell'atleta \n --> "))
    if Salto>=0.01:
        print("La misura del salto dell'atleta interessato è pari a" ,Salto, "metri")
        Natleti=Natleti-1
    else:
        print("Dati errati")
        break
