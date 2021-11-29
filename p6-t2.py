import matplotlib.pyplot as plt
import decimal
import numpy as np
from math import sqrt 

n = int(input())
def parabola_plotter(a=1, b=1, c=0, title='parabola  plotter'):
  if n <= 1:
    x = np.arange(-10,10,0.01)

    y = a*x**2 + b*x + c

    plt.plot(x, y, label='my parabola', marker='>', ms=5)
    plt.title(title)
    
  if n > 1:
    
    x = np.arange(-10,10,0.01)
  
    #y = 1 + x**2 * b**2
    y = np.sqrt((x**2/a**2-1)*b**2 )

    plt.plot(x, y, label='my giperbola', marker='>', ms=1)
    plt.plot(x, -y, label='my giperbola', marker='>', ms=1)
    plt.show()
    plt.title(title)

  plt.xlabel('coord: x')
  plt.ylabel('coord: y')
  plt.title(title)
  plt.show()
  plt.legend()
parabola_plotter()
