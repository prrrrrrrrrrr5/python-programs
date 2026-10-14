import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle
import random

# Dimensioni del contenitore
WIDTH = 10
HEIGHT = 10

def urto_elastico(v1, v2, m1, m2):
    vf1 = ((m1 - m2) * v1 + 2 * m2 * v2) / (m1 + m2)
    vf2 = ((m2 - m1) * v2 + 2 * m1 * v1) / (m1 + m2)
    return vf1, vf2

class Ball:
    def __init__(self, x, y, vx, vy, r, m, color):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.r = r
        self.m = m
        self.color = color
        self.circle = Circle((self.x, self.y), self.r, fc=self.color)

    def move(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.circle.center = (self.x, self.y)

    def check_wall_collision(self):
        if self.x - self.r < 0:
            self.x = self.r
            self.vx *= -1
        elif self.x + self.r > WIDTH:
            self.x = WIDTH - self.r
            self.vx *= -1

        if self.y - self.r < 0:
            self.y = self.r
            self.vy *= -1
        elif self.y + self.r > HEIGHT:
            self.y = HEIGHT - self.r
            self.vy *= -1

    def collide(self, other):
        dx = other.x - self.x
        dy = other.y - self.y
        dist2 = dx * dx + dy * dy
        distance = dist2 ** 0.5
        if distance == 0 or distance >= self.r + other.r:
            return

        # Versore della direzione di collisione
        nx = dx / distance
        ny = dy / distance

        # Velocità relative proiettate sulla direzione della collisione
        v1n = self.vx * nx + self.vy * ny
        v2n = other.vx * nx + other.vy * ny

        # Componenti tangenziali restano invariate (urto elastico solo lungo la normale)
        vt1x = self.vx - v1n * nx
        vt1y = self.vy - v1n * ny
        vt2x = other.vx - v2n * nx
        vt2y = other.vy - v2n * ny

        # Nuove velocità lungo la normale
        v1n_final, v2n_final = urto_elastico(v1n, v2n, self.m, other.m)

        # Combinazione delle componenti tangenziali e nuove normali
        self.vx = vt1x + v1n_final * nx
        self.vy = vt1y + v1n_final * ny
        other.vx = vt2x + v2n_final * nx
        other.vy = vt2y + v2n_final * ny

        # Correggiamo sovrapposizione
        overlap = 0.5 * (self.r + other.r - distance + 1e-6)
        self.x -= overlap * nx
        self.y -= overlap * ny
        other.x += overlap * nx
        other.y += overlap * ny

def crea_palle(n):
    palle = []
    max_attempts = 1000
    r = 0.3

    for _ in range(n):
        for _ in range(max_attempts):
            x = random.uniform(r, WIDTH - r)
            y = random.uniform(r, HEIGHT - r)
            overlap = False
            for b in palle:
                dx = x - b.x
                dy = y - b.y
                if (dx**2 + dy**2)**0.5 < 2*r:
                    overlap = True
                    break
            if not overlap:
                break
        vx = random.uniform(-1, 1)
        vy = random.uniform(-1, 1)
        m = 1
        color = (random.random(), random.random(), random.random())
        palle.append(Ball(x, y, vx, vy, r, m, color))
    return palle

# Main
fig, ax = plt.subplots()
ax.set_xlim(0, WIDTH)
ax.set_ylim(0, HEIGHT)
ax.set_aspect('equal')
ax.set_facecolor('white')

balls = crea_palle(10)
for ball in balls:
    ax.add_patch(ball.circle)

def update(frame):
    for ball in balls:
        ball.move(0.05)
        ball.check_wall_collision()
    for i in range(len(balls)):
        for j in range(i + 1, len(balls)):
            balls[i].collide(balls[j])
    return [ball.circle for ball in balls]

ani = animation.FuncAnimation(fig, update, frames=300, interval=20, blit=True)
plt.show()