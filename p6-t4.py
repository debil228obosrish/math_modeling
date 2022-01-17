import matplotlib.pyplot as plt
import numpy as np

def circle (radius=2):
  x= np.arange(-2*radius,2*radius,0.1)

  y =np.arange(-2*radius,2*radius,0.1)
  X,Y = np.meshgrid(x,y)
  fxy = X**2 + Y**2
  plt.contour (X, Y, fxy, levels=[radius**2] )
  plt.show()

def circle2 (radius=10):
  x= np.arange(-20*radius,20*radius,0.1)
  y =np.arange(-20*radius,20*radius,0.1)
  a = 20
  b = 10
  X,Y = np.meshgrid(x,y)
  fxy = X**2/a**2 + Y**2/b**2
  plt.contour (X, Y, fxy, levels=[radius**2] )
  plt.axis('equal')
  plt.show()
n = int(input())
if (n==1):
  circle()
elif (n==2):
  circle2()