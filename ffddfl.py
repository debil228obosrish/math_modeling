import numpy as np
import matplotlib.pyplot as plt

circle1 = plt.Circle((10 , 10), 1, color='y',fill=False)

  

fig, ax = plt.subplots() 
ax.set_xlim((0, 20))
ax.set_ylim((0, 20))
ax.add_artist(circle1)

fig.savefig('plotcircles12.png')