import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

fig=plt.figure()
ax=plt.axes(xlim=(0, 4), ylim=(-2, 2))
line,=ax.plot([], [], lw=3, color="b")
line2, =ax.plot([], [], lw=3, color="c")
line3, =ax.plot([], [], lw=3, color="m")


def init():
    line.set_data([], [])
    return line,
def animate(i):
    x=np.linspace(0,4,1000)
    y=np.sin(1*np.pi*(x-0.02*i))
    y2=np.sin(1*np.pi*(x+0.02*i))
    y3=y+y2
    line.set_data(x, y)
    line2.set_data(x, y2)
    line3.set_data(x, y3)
    return line,

anim = FuncAnimation(fig, func=animate, init_func=init, frames=200, interval=20)