'''
Fornito in input un numero >=0 di 4 cifre specificare, fornendo un messaggio opportuno, se si tratta di un anno bisestile oppure no.
Specificato che è secolare ogni anno che rappresenta il primo anno di un secolo (dunque 1800, 1900, 2000 etc.. sono anni secolari), si ricorda che sono bisestili:
• tutti gli anni non secolari divisibili per 4 e
• gli anni secolari divisibili per 400
dunque
l’anno 2020 è un anno bisestile (non è secolare ed è divisibile per 4)
l’anno 2000 è un anno bisestile ( è secolare ma è divisibile per 400)
l’anno 1900 non è un anno bisestile ( è secolare ma non è divisibile per 400)
l’anno 2018 non è un anno bisestile ( non è divisibile per 4)
'''

Anno=int(input("Inserisci di seguito l'anno che vuoi analizzare \n --> "))
if Anno%100==0:
    print("Quest'anno è secolare")
    if Anno%400==0:
        print("Quest'anno è bisestile")
    else:
        print("Quest'anno non è bisestile")
else:
    print("Quest'anno non è secolare")
    if Anno%4==0:
        print("Quest'anno è bisestile")
    else:
        print("Quest'anno non è bisestile")
