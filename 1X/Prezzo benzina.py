print("Questo programma serve per calcolare quanto spendi di benzina se prendi un modello di auto Ada o un modello di auto Baba")

Modello=str(input("Scrivi il modello da te scelto (le risposte possibili sono: Ada, Baba) --> "))
Risposta1= "Ada"
Risposta2= "Baba"
Kilometri=float(input("Scrivi di seguito quanti Km vuoi fare "))
PrezzoBenzina=float(input("Infine scrivi il prezzo della benzina al litro --> "))
if Modello==Risposta1:
    Prezzo=(Kilometri/18)*1.455
    print("Il prezzo da pagare per il viaggio è" ,Prezzo, ("€"))
elif Modello==Risposta2:
    Prezzo=(Kilometri/22)*1.455
    print("Il prezzo da pagare per il viaggio è" ,Prezzo, ("€"))
