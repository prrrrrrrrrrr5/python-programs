import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parametri
R, C, V0 = 10e3, 100e-9, 5
dt = 1e-6
tau = R * C
tCh = 5 * tau
tDis = 5 * tau

n1 = int(tCh / dt)
n2 = int(tDis / dt)

# Prepara i dati
t = np.zeros(n1 + n2)
q = np.zeros(n1 + n2)

for k in range(1, n1):
    q[k] = q[k - 1] * (1 - dt / tau) + (V0 / R) * dt
    t[k] = t[k - 1] + dt

for k in range(n1, n1 + n2):
    q[k] = q[k - 1] * (1 - dt / tau)
    t[k] = t[k - 1] + dt

# Imposta la figura
fig, ax = plt.subplots(figsize=(8, 5))
ax.set_xlim(0, t[-1])
ax.set_ylim(0, V0 * C)
line, = ax.plot([], [], lw=2, label="RC")
ax.set_xlabel("Tempo (s)")
ax.set_ylabel("Carica (q)")
ax.set_title("Carica e scarica di un condensatore")
ax.grid(True)
ax.legend()

# Inizializza l'animazione
def init():
    line.set_data([], [])
    return line,

# Funzione di aggiornamento
def update(frame):
    line.set_data(t[:frame], q[:frame])
    return line,

# Crea l'animazione
ani = animation.FuncAnimation(fig, update, frames=len(t), init_func=init, blit=True, interval=1, repeat=False)

plt.show()
