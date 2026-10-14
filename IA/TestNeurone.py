from Neurone import *

neurone=Neurone()
while True:
    print("--> ", end ="\t")
    domanda=input("").lower()
    if domanda=="basta":
        break
    neurone.risposta(domanda)
