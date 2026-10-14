import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig=plt.figure()
a=20
ax=plt.axes(xlim=(-a,a), ylim=(0,a))
line,=ax.plot([],[],lw=3, color='g')
line2,=ax.plot([],[],lw=3, color='r')

amp=1
k=10.66
w=3.198
L=100
D=4
Nt=1000
dt=0.01
E=1
y=np.linspace(-a,a,1000)


#coordinate sorgente 1
xS1=0
yS1=D

#coordinate sorgente 2
xS2=0
yS2=-D

#coordinate punto generuci

#I1=np.sqrt(((x-D)**2+L**2)
#I1=np.sqrt(((x+D)**2+L**2)

r1=np.sqrt(L**2+(D-y))
r2=np.sqrt(L**2+(D-y))

def sommatoria(Nt,I):
    somma=0
    for i in range(Nt):
        somma+=I
    return somma

def init():
    line.set_data([], [])
    line2.set_data([], [])
    return line,line2,

def animate(i):
    t=0.01*i
    E1=E*np.cos(k*r1-w*t) #Equazione prima onda
    E2=E*np.cos(k*r2-w*t) #Equazione seconda onda
    I=(E1+E2)**2 #Intensità instantanea della luce (Eq. 1)
    Im=(1/Nt)*sommatoria(Nt,I) #Intensità media (Eq. 2)
    It=2*(E**2)*(np.cos((k*D*y)/L)**2) #Intensità teorica (Eq. 3)
    line.set_data(y,Im)
    line2.set_data(y,It)
    
    return line,

anim = FuncAnimation(fig, func=animate, init_func=init, frames=200, interval=20)

