import math
g = 10
def kinemathick(m, v):
  return (m * v**2)/2
def potential(m, g, h):
  return m * g * h

m = 20
v = 30
h = 15  

E = kinemathick(m, v) + potential(m, g, h)
print(E)