import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

def Fourier(T,teta,nmax):
    #nmax=99
    k = np.arange(1, nmax)
    k = 2 * k - 1
    f = np.zeros_like(teta)

    for i, ti in enumerate(teta):
        f[i] = np.sum(np.sin(k * ti)/k)

    f = (4 / np.pi) * f
    return f

# Definire i parametri iniziali
T = 2 * np.pi  # Periodo dell'onda
teta = np.linspace(-T,T, 201)
nmax=1

#Disegnare l'onda quadra
x = np.linspace(-T, T, 1000)  # Intervallo su cui valutare la funzione
y = np.sign(np.sin(x))


#Fourier iniziale
fourier=Fourier(T,teta,nmax)

# Creare la figura e gli assi
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.1, bottom=0.25)  # Regolare gli spazi per gli slider
line1, = plt.plot(teta, fourier, lw=2)
line2, = plt.plot(x,y)
ax=plt.subplot(111)
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))
ax.spines[['top','right']].set_visible(False)
#impostazione delle tacche dell'asse y
ax.set_yticks([-1.5,-1, 0, 1, 1.5])
ax.set_yticklabels(['-1,5','-1', '0', '1', '1,5'])
#impostazione delle tacche dell'asse x
ax.set_xticks([-2*np.pi, -np.pi,0,np.pi,2*np.pi])
ax.set_xticklabels(['-2$\Pi$','-$\Pi$','0','$\Pi$','2$\Pi$'])

plt.grid(True)

#CREAZIONE SLIDER PER nmax
ax_nmax = plt.axes([0.1, 0.15, 0.65, 0.03]) # Posizione dell'asse per lo slider di m

# Slider per nmax (numero coefficienti Fourier)
slider_nmax = Slider(ax=ax_nmax, label='N', valmin=1, valmax=1000, valinit=1)

# Funzione per aggiornare il grafico con i nuovi parametri
def update(val):
    nmax_new = slider_nmax.val  # Ottieni il valore corrente di nmax
    f=Fourier(T,teta,nmax_new)
    line1.set_ydata(f)  # Aggiorna i dati della funzione Fourier
    fig.canvas.draw_idle()  # Aggiorna il grafico in tempo reale

# Collegare gli slider alla funzione di aggiornamento
slider_nmax.on_changed(update)

plt.plot(x,y)
plt.show()