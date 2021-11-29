import matplotlib.pyplot as plt
import numpy as numpy

x = [1, 5, 5, 1, 1]
y = [5, 5, 1, 1, 5]

plt.plot(x, y, color='g', label='lunhte', marker='>', ms = 5)

plt.xlabel('coord: x')
plt.ylabel('coord: y')
plt.legend()
plt.title('base')
plt.grid()
plt.show()