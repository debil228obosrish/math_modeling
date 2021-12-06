import matplotlib.pyplot as plt
import numpy as np
import math
from math  import sqrt
n = int(input()) 
b=0.02
N=1000
phi0=0.01
phi1=8*math.pi
phi= np.linspace(phi0,phi1,N)
if(n==1):
  r=np.exp(b*phi)
if(n==2):
  r=b*phi
if(n==3):
  r=b/(np.sqrt(phi))
if(n==4):
  r=np.sin(b*phi)
x=[]
y=[]
for i in range (N):
  x.append(r[i]*np.cos(phi[i]))
  y.append(r[i]*np.sin(phi[i]))
plt.plot(x,y)
plt.axis('equal')
plt.show()