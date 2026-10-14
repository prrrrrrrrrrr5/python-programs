#Inizio
def inserimento(lg):
    l=[]
    avanti="si"
    m=int(input("Quante provincie vuoi inserire? \n --> "))
    for i in range(m):
        l.append(input("Inserisci una provincia \n -->"))
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
    n=len(lg[0])
    for i in range(len(lg)):
        media=0
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
