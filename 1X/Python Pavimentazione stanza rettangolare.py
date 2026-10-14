print("Questo programma serve per calcolare quanto costa pavimentare una stanza di forma rettangolare")

A=float(input("Per prima cosa inserisci la lunghezza di un lato della stanza "))

B=float(input("Ora digita la lunghezza dell'altro lato "))

Metriquadri=(A*B)/10000

Pavimentazione=float(input("Bene ora digita il costo della pavimentazione in metri quadri "))

print("Ora uscirà il costo totale" ,Metriquadri*Pavimentazione, "€")
