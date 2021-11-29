import matplotlib.pyplot as plt 
import numpy as np 

def circle_plotter(radius=10):
  x = np.arrange(-2*radius, 2*radius, 0.1)
  y = np.arrange(-2*radius, 2*radius, 0.1)

  x, y = np.meshgrid(x, y)

  fxy = x**2 + y**2

  plt.contour(x, y, fxy, levels=[radius**2])