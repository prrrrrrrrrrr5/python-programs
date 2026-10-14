import numpy as np
import matplotlib.pyplot as plt
#Es. 1
# quadrato=np.zeros([64,64,3],dtype=np.uint8)
# quadrato[:,:]=[0,0,0]
# quadrato[16:48,16:48]=[255,255,255]


#Es. 2
# quadrato=np.zeros([64,64,3],dtype=np.uint8)
# cont=0
# y=0
# x=8
# for i in range(8):
#     if cont%2==0:
#         quadrato[:,y:x]=[255,255,255]
#     else:
#         quadrato[:,y:x]=[0,0,0]
#     x+=8
#     y+=8
#     cont+=1

#Es. 3
# quadrato=np.zeros([64,64,3],dtype=np.uint8)
# n=int(input("Inserisci il numero di colonne \n --> "))
# x=int(input("Quanto vuoi grande la figura nelle x? \n --> "))
# y=int(input("Quanto vuoi grande la figura nelle y? \n --> "))

# c=int(y/n)
# cont=0
# b=0
# a=c
# quadrato=np.zeros([x,y,3],dtype=np.uint8)
# quadrato[:,:]=[255,255,255]
# for i in range(n):
#     if cont%2==1:
#         quadrato[:,b:a]=[0,0,0]
#     b+=c
#     a+=c
#     cont+=1

#Es. 4
# quadrato=np.zeros([64,64,3],dtype=np.uint8)
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
quadrato=np.zeros([64,64,3],dtype=np.uint8)
quadrato[:,:]=[255,255,255]
x=0
y=8
a=0
b=8
cont=0
for i in range(8):
    for j in range(8):
        if cont%2==0:
            quadrato[a:b,x:y]=[0,0,0]
        x+=8
        y+=8
        cont+=1
    cont+=1
    x=0
    y=8
    a+=8
    b+=8
    
#Es. 6
# quadrato=np.zeros([64,64,3],dtype=np.uint8)
# quadrato[:,:]=[255,255,255]
# quadrato[30:35,18:46]=[0,0,0]
# quadrato[8:13,18:46]=[0,0,0]
# quadrato[8:58,18:23]=[0,0,0]

#Es. 7
# quadrato=np.zeros([64,64,3],dtype=np.uint8)
# quadrato[:,:]=[0,0,0]
# quadrato[30:35,18:46]=[255,255,255]
# quadrato[8:13,18:46]=[255,255,255]
# quadrato[8:58,18:23]=[255,255,255]

#Es. 8
# quadrato=np.zeros([64,64,3],dtype=np.uint8)
# quadrato[:,:]=[0,0,0]
# quadrato[18:46,30:35]=[255,255,255]
# quadrato[18:46,8:13]=[255,255,255]
# quadrato[18:23,8:58]=[255,255,255]

#Es. 9.1
# quadrato=np.zeros([64,64,3],dtype=np.uint8)
# quadrato[:,:]=[255,255,255]
# quadrato[18:46,30:35]=[0,0,0]
# quadrato[18:46,53:58]=[0,0,0]
# quadrato[18:23,8:58]=[0,0,0]

#Es. 9.2
# quadrato=np.zeros([64,64,3],dtype=np.uint8)
# quadrato[:,:]=[255,255,255]
# quadrato[30:35,18:46]=[0,0,0]
# quadrato[53:58,18:46]=[0,0,0]
# quadrato[8:58,18:23]=[0,0,0]

#Es. 9.3
# quadrato=np.zeros([64,64,3],dtype=np.uint8)
# quadrato[:,:]=[255,255,255]
# quadrato[30:35,18:46]=[0,0,0]
# quadrato[8:13,18:46]=[0,0,0]
# quadrato[8:58,41:46]=[0,0,0]

plt.imshow(quadrato)
plt.show()