import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

fig, ax = plt.subplots()
dots, = plt.plot([], [], '--', color='red', label='line')

theta = np.linspace(0, 2*np.pi, 20)
radius = 2
a = radius*np.cos(theta)
b = radius*np.sin(theta)



circle1 = plt.Circle((16 , 40), 2, color='y',fill=False)
fig, ax = plt.subplots() 
ax.set_xlim((0, 20))
ax.set_ylim((0, 20))
#ax.add_artist(circle1)
dots2, = plt.plot(a, b, '--', color='blue', label='line')

def animate(i):
    dots.set_data(a + i, b)

ani = animation.FuncAnimation(fig,
                        animate,
                        
                        frames=100,
                        interval=30)


def parabola_plotter(a=0.1, b=0.1, c=5, title='parabola  plotter'):
    x = np.arange(-20,20,0.1)
    y = a*x**2 + b*x + c

    plt.plot(x, y, label='my parabola', marker='>', ms=0.1)
    plt.title(title)
#parabola_plotter()
plt.axis('equal')
plt.show()
ani.save('my_anim.gif')

circle()
