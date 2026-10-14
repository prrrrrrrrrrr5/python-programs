#Inizio

m=int(input("Inserisci di seguito il primo numero \n --> "))
while m<0:
    m=int(input("Inserisci di seguito il primo numero maggiore o uguale a 0 \n --> "))
n=int(input("Inserisci di seguito il secondo numero (maggiore del primo) \n --> "))
while n<0 or n<m:
    n=int(input("Inserisci di seguito il secondo numero maggiore del primo e maggiore o uguale a 0 \n --> "))
print("I numeri dispari tra il primo ed il secondo numero inseriti sono:")
print(" ")
for i in range(m,n+1):
    if m%2==1:
        print(m)
        m=m+1
    elif m%2==0:
        print(" ")
        m=m+1
#Fine
