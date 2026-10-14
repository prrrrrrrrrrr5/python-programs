#Inizio
def cerca(lg):
    global presente
    presente=False
    for i in range(len(lg)):
        if provincia in lg:
            presente=True
            print("Provincia già inserita")
        else:
            presente=False
    return presente

def inserimento(lg):
    l=[]
    avanti="si"
    global provincia
    provincia=""
    m=int(input("Quante provincie vuoi inserire? \n --> "))
    for i in range(m):
        provincia=input("Inserisci una provincia \n -->")
        cerca(lg)
        if presente==False:
            l.append(provincia)
            while avanti=="si":
                Input=input("Inserisci una temperatura \n --> ")
                if Input=="no" or Input=="No" or Input=="nO":
                    avanti="no"
                else:
                    l.append(int(Input))
                    avanti="si"
        lg.append(l)
        avanti="si"
        l=[]

def mediaProvincie(lg):
    for i in range(len(lg)):
        media=0
        n=len(lg[i])
        for j in range(1,n):
            media+=lg[i][j]
        media/=(n-1)
        print(lg[i][0],media)

lg=[]
inserimento(lg)
media=0
for i in range(len(lg)):
    media+=lg[i][1]
mediaProvincie(lg)
media/=len(lg)
print(media)
#Fine
