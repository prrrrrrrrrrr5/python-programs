import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Costanti
R, C, V = 10e3, 100e-6, 5
tau = R * C

# Tempo simulazione
t = np.linspace(0, 10 * tau, 1000)
t_half = t[len(t) // 2]  # Punto di transizione

def carica(t):
    return V * (1 - np.exp(-t / tau))

def scarica(t, v0):
    return v0 * np.exp(-t / tau)

# Impostazione della figura
fig, ax = plt.subplots()
ax.set_xlim(0, t[-1])
ax.set_ylim(0, V + 0.5)
line, = ax.plot([], [], 'b-', lw=2)

def init():
    line.set_data([], [])
    return line,

def update(frame):
    xdata = t[:frame]
    v0 = carica(t_half)  # Punto finale della carica
    ydata = np.where(t[:frame] < t_half, carica(t[:frame]), scarica(t[:frame] - t_half, v0))
    line.set_data(xdata, ydata)
    return line,

ani = animation.FuncAnimation(fig, update, frames=len(t), init_func=init, blit=True, interval=10)

plt.show()
