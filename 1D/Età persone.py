'''
<<Note (quindi acquisibili in input) l’età di un gruppo di persone, delle quali
non è noto il numero all’inizio dell’elaborazione, restituisci in output il
numero di persone maggiorenni.>>
'''

#Inizio

Domanda=str(input("Vuoi inserire l'età di una persona? (S/N) \n --> "))
Maggiorenni=0

while Domanda=="S":
    Eta=int(input("Inserisci di seguito l'età di una persona \n --> "))
    if Eta>=18:
        Maggiorenni=Maggiorenni+1
    Domanda=str(input("Vuoi inserire l'età di una persona? (S/N) \n --> "))

#Fine mentre

print("Il numero di persone maggiorenni è pari a" ,Maggiorenni)

#Fine
