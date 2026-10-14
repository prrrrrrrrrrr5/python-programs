import numpy as np
import matplotlib.pyplot as plt
#Es. 1
quadrato=np.zeros([64,64,3],dtype=np.uint8)
'''
quadrato[:,:]=[0,0,0]
quadrato[16:48,16:48]=[255,255,255]
'''

#Es. 2
'''
cont=0
y=0
x=8
for i in range(8):
    if cont%2==0:
        quadrato[:,y:x]=[255,255,255]
    else:
        quadrato[:,y:x]=[0,0,0]
    x+=8
    y+=8
    cont+=1
'''
#Es. 3
'''
n=int(input("Inserisci il numero di colonne \n --> "))
x=int(input("Quanto vuoi grande la figura nelle x? \n --> "))
y=int(input("Quanto vuoi grande la figura nelle y? \n --> "))

c=int(y/n)
cont=0
b=0
a=c
quadrato=np.zeros([x,y,3],dtype=np.uint8)
quadrato[:,:]=[255,255,255]
for i in range(n):
    if cont%2==1:
        quadrato[:,b:a]=[0,0,0]
    b+=c
    a+=c
    cont+=1
'''
#Es. 4
# quadrato[:,:]=[255,255,255]
# x=0
# y=8
# a=0
# b=8
# cont=0
# for i in range(8):
#     for j in range(8):
#         if cont%2==0:
#             quadrato[a:b,x:y]=[0,0,0]
#         x+=8
#         y+=8
#         cont+=1
#     cont+=1
#     x=0
#     y=8
#     a+=8
#     b+=8
#     print(i)

#Es. 5

#Es. 6
quadrato=np.zeros([64,64,3],dtype=np.uint8)
quadrato[:,:]=[255,255,255]


plt.imshow(quadrato)
plt.show()
