import matplotlib
import matplotlib.pyplot as plt
import numpy as np



def circle (radius=10):
  x= np.arange(-2*radius,2*radius,0.1)

  y =np.arange(-2*radius,2*radius,0.1)
  X,Y = np.meshgrid(x,y)
  fxy = X**2 + Y**2
  plt.contour (X, Y, fxy, levels=[radius**2] )
  plt.axis('equal')

  def parabola_plotter(a=0.5, b=0.5, c=0, title='parabola  plotter'):
    x = np.arange(-10,10,0.0001)
    y = a*x**2 + b*x + c

    plt.plot(x, y, label='my parabola', marker='>', ms=0.1)
    plt.title(title)
  parabola_plotter()

  plt.show()
circle()


