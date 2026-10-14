import random
#Inizio

def F(x,y,listay):
    for i in range((x[1]-x[0])+1):
        y=(1/2)*(i+x[0])+4
        listay.append(y)

def monteCarlo(listay,dentro,fuori):    
    area=0
    for i in range(0,6):
        for j in range(len(listay)):
            y2=random.randint(5,12)
            if y2<listay[j]:
                dentro+=1
            else:
                fuori+=1
    area=35*dentro/fuori
    print("La probabile area del rettangolo è" ,area, "cm^2")

x=[5,10]
y=0
listay=[]
F(x,y,listay)
dentro=0
fuori=0
monteCarlo(listay, dentro, fuori)

#Fine
