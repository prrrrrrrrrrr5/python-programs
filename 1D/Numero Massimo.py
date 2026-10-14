'''
<<Noti tre numeri, non necessariamente interi calcolare e mostrare in output il maggiore dei tre>>
'''

#Inizio

PrimoNumero=float(input("Inserisci di seguito il valore del primo numero \n --> "))
SecondoNumero=float(input("Bene, ora inserisci il valore del secondo numero \n --> "))
TerzoNumero=float(input("Per finire inserisci il valore del terzo numero \n --> "))

NumeroMax=PrimoNumero
if SecondoNumero>PrimoNumero and SecondoNumero>TerzoNumero:
    NumeroMax=SecondoNumero
elif TerzoNumero>SecondoNumero and TerzoNumero>PrimoNumero:
    NumeroMax=TerzoNumero

print("Il numero maggiore tra i tre è" ,NumeroMax)

#Fine
