# Programma ideato e creato da Favalli Ivan
print("Questo programma serve per classificare un triangolo in base all'ampiezza degli angoli")

Ampiezza1=float(input("Inserisci di seguito l'ampiezza del primo angolo in gradi (non mettere il simbolino dei gradi) --> "))
Ampiezza2=float(input("Inserisci di seguito l'ampiezza del secondo angolo in gradi (non mettere il simbolino dei gradi) --> "))
Ampiezza3=float(input("Inserisci di seguito l'ampiezza del terzo angolo in gradi (non mettere il simbolino dei gradi) --> "))

if Ampiezza1<90 and Ampiezza2<90 and Ampiezza3<90: # Un triangolo acutangolo ha tutti gli angoli inferiori di 90°, per cui in questa riga ho detto: se tutti gli angoli sono inferiori a 90°, allora scrivi che è acutangolo
    print("Quest'angolo è acutangolo")
elif Ampiezza1>90 and Ampiezza2>90: #In queste 15 righe ci sono tutti i casi in cui gli angoli scritti non portano ad un triangolo
    print("Non è un angolo")
elif Ampiezza1>90 and Ampiezza3>90:
    print("Non è un angolo")
elif Ampiezza3>90 and Ampiezza2>90:
    print("Non è un angolo")
elif Ampiezza1>90 and Ampiezza2>90 and Ampiezza3>90 :
    print("Non è un angolo")
elif Ampiezza1==90 and Ampiezza2==90:
    print("Non è un angolo")
elif Ampiezza1==90 and Ampiezza3==90:
    print("Non è un angolo")
elif Ampiezza3==90 and Ampiezza2==90:
    print("Non è un angolo")
elif Ampiezza1==90 and Ampiezza2==90 and Ampiezza3==90 :
    print("Non è un angolo")
elif Ampiezza1==90 or Ampiezza2==90 or Ampiezza3==90: # Un triangolo rettangolo ha solo un angolo superiore di 90°, per cui in questa riga ho detto: se un angolo è uguale a 90°, allora scrivi che è rettangolo
    print("Quest'angolo è rettangolo")
elif Ampiezza1>90 or Ampiezza2>90 or Ampiezza3>90: # Un triangolo ottusangolo ha solo un angolo superiore di 90°, per cui in questa riga ho detto: se un angolo è superiore a 90°, allora scrivi che è ottusangolo
    print("Quest'angolo è ottusangolo")
