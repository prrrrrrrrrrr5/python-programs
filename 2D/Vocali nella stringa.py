x=input("Inserisci la stringa \n --> ")
l=len(x)
while l<8:
    x=input("Inserisci la stringa \n --> ")
    l=len(x)
caratteri="aeiouAEIOU"
nvocali=0
stringaf=""
for i in range(1, l):
    if x[i] in caratteri:
        nvocali+=1
        stringaf=stringaf+x[i]
if len(stringaf)!=l:
    print("Il numero dei caratteri non vocali nella stringa è" ,l-len(stringaf))
else:
    if 