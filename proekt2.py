import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
n = int(input("Введите число:"))
fig, ax = plt.subplots()
if n <= 1:
  def parabola_plotter(a=0.1, b=0.1, c=5, title='parabola  plotter'):
    x = np.arange(-20,20,0.5)
    y = a*x**2 + b*x + c
    plt.plot(x, y, label='my parabola', marker='>', ms=0.1)
    plt.title(title)
    return [x, y]

  dots, = plt.plot([], [], '--', color='red', label='line')

  theta = np.linspace(0, 2*np.pi, 20)
  radius = 2
  a = radius*np.cos(theta)
  b = radius*np.sin(theta)

  p = parabola_plotter()
  frames = len(p[0])
  ax.set_xlim((0, 20))
  ax.set_ylim((0, 20))


  def animate(i):
      dots.set_data(a + p[0][i], b + p[1][i])

  ani = animation.FuncAnimation(fig,
                        animate,
                        
                        frames=frames,
                        interval=30)
if n > 1:
  def parabola_plotter(a=0.1, b=0.1, c=5, title='parabola  plotter'):
    x = np.arange(-20,20,0.5)
    y = -a*x**2 + b*x + c
    plt.plot(x, y, label='my parabola', marker='>', ms=0.1)
    plt.title(title)
    return [x, y]

  dots, = plt.plot([], [], '--', color='red', label='line')

  theta = np.linspace(0, 2*np.pi, 20)
  radius = 2
  a = radius*np.cos(theta)
  b = radius*np.sin(theta)

  p = parabola_plotter()
  frames = len(p[0])
  ax.set_xlim((0, 20))
  ax.set_ylim((0, 20))


  def animate(i):
      dots.set_data(a + p[0][i], b + p[1][i])

  ani = animation.FuncAnimation(fig,
                        animate,
                        
                        frames=frames,
                        interval=30)


plt.axis('equal')
ani.save('my_anim.gif')
#визуализация движения по криволинейной траектории