import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation


fig, ax = plt.subplots()

a = np.array([ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 ])
b= np.array([ 20 , 30 , 5 , 12 , 39 , 48 , 50 , 3 ])
# Plotting the Graph
plt.plot(a, b)
plt.title( "Curve plotted using the given points" )
plt.xlabel( "a" )
plt.ylabel( "b" )

dots, = plt.plot([], [], '--', color='red', label='line')

theta = np.linspace(0, 2*np.pi, 20)
radius = 2
a = radius*np.cos(theta)
b = radius*np.sin(theta)

frames = len(p[0])
ax.set_xlim((0, 20))
ax.set_ylim((0, 20))


def animate(i):
    dots.set_data(a + p[0][i], b + p[1][i])

ani = animation.FuncAnimation(fig,
                        animate,
                        
                        frames=frames,
                        interval=30)
fig, ax = plt.subplots()

                        
                        
plt.axis('equal')
ani.save('my_anim.gif')
plt.show()