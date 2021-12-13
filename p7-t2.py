import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
 
fig, ax = plt.subplots()
line, = plt.plot([], [], '--', color='green', label='line')
 
edge = 10
 
plt.axis('equal')
 
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
 
x, y = [], []
 
alpha = 0.15
t = np.arange(0, 2*np.pi, 0.1)
sin_t = np.sin(t)
cos_t = np.cos(t)
 
def animate(frame):
    R = frame*alpha
    x = R*sin_t
    y = R*cos_t
    line.set_data(x, y)
 
ani = animation.FuncAnimation(fig,
                        animate,
                        frames=100,
                        interval=30)
 
ani.save('my_anim_ex2.gif')