import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.animation import FuncAnimation

# Parametri iniziali
dt = 0.05
raggio = 1

# Posizione iniziale
x, y = -3.0, -3.0
x2, y2 = 3.0, 3.0

# Velocità iniziale
vx, vy = 4.0, 3.0
vx2, vy2 = 5.0, 2.0

# Limiti dell'area di movimento
xlim = (-10, 10)
ylim = (-7, 7)

# Setup figura e asse
fig, ax = plt.subplots()
ax.set_xlim(xlim)
ax.set_ylim(ylim)
ax.set_aspect('equal')
ax.set_title('Urto elastico 2D - Palline')

# Crea le palline
pallina = Circle((x, y), raggio, color='orange')
ax.add_patch(pallina)
pallina2 = Circle((x2, y2), raggio, color='blue')
ax.add_patch(pallina2)

# Funzione per calcolare la collisione elastica con formula corretta
def elastic_collision(vx1, vy1, vx2, vy2, x1, y1, x2, y2):
    # Vettore di separazione
    dx = x2 - x1
    dy = y2 - y1
    dist_sq = dx**2 + dy**2  # distanza al quadrato tra i centri
    
    # Se la distanza tra i centri è inferiore o uguale alla somma dei raggi, avviene la collisione
    if dist_sq <= (2 * raggio)**2:
        # Calcolo della velocità finale
        # Prodotto scalare tra la velocità relativa e il vettore di separazione
        dot_product = (vx1 - vx2) * dx + (vy1 - vy2) * dy
        dist = np.sqrt(dist_sq)
        
        # Calcola la componente della velocità lungo la direzione della separazione
        factor = 2 * dot_product / dist_sq
        
        # Aggiorna le velocità lungo la direzione della separazione
        vx1 -= factor * dx / dist
        vy1 -= factor * dy / dist
        vx2 += factor * dx / dist
        vy2 += factor * dy / dist
        
    return vx1, vy1, vx2, vy2

# Funzione di aggiornamento per l'animazione
def update(frame):
    global x, y, vx, vy, x2, y2, vx2, vy2

    # Controllo urti con i bordi
    if x + raggio >= xlim[1] or x - raggio <= xlim[0]:
        vx *= -1
    if y + raggio >= ylim[1] or y - raggio <= ylim[0]:
        vy *= -1
    if x2 + raggio >= xlim[1] or x2 - raggio <= xlim[0]:
        vx2 *= -1
    if y2 + raggio >= ylim[1] or y2 - raggio <= ylim[0]:
        vy2 *= -1

    # Controllo collisione elastica tra le due palline
    vx, vy, vx2, vy2 = elastic_collision(vx, vy, vx2, vy2, x, y, x2, y2)

    # Aggiornamento delle posizioni
    x += vx * dt
    y += vy * dt
    x2 += vx2 * dt
    y2 += vy2 * dt

    # Aggiorna la posizione delle palline
    pallina.center = (x, y)
    pallina2.center = (x2, y2)

    return pallina, pallina2

# Crea l'animazione
ani = FuncAnimation(fig, update, frames=600, interval=30, blit=True)
plt.show()
