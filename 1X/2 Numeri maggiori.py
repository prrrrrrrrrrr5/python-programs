#Questo programma serve per scrivere i due numeri maggiori tra 2 N numeri inseriti dall'utente
print("Questo programma serve per scrivere i due numeri maggiori tra 2 N numeri inseriti dall'utente")

Numeri=int(input("Inserisci di seguito quanti numeri vuoi inserire --> ")) #Questa riga serve per chiedere all'utente quanti numeri vuole inserire
Numero1=int(input("Inserisci di seguito un numero --> ")) #Primo numero inserito che servirà per dare un valore alle variabili dei numeri maggiori
NumeroMax1=Numero1 #Variabili che serviranno per trovare i due numeri maggiori
NumeroMax2=Numero1
PosizioneNM1=1
PosizioneNM2=1
for i in range(1,Numeri): #Ciclo che serve per far inserire all'utente i numeri mancanti
    Numero=int(input("Inserisci di seguito un numero --> "))
    if Numero>NumeroMax1: #Le prossime righe servono per aumentare i 2 numeri maggiori affinchè il programma funzioni correttamente
        NumeroMax2=NumeroMax1
        NumeroMax1=Numero
        PosizioneNM1=i
    elif Numero>NumeroMax2 and Numero<NumeroMax1:
        NumeroMax2=Numero
        PosizioneNM2=i
print("Il numero maggiore è" ,NumeroMax1, "ed il secondo maggiore è" ,NumeroMax2,)
