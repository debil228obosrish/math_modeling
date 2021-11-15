import numpy as np
import random as rnd

N = 10

def mpl(a):
    s = 1
    for i in range(N):
        s *= a[i]
    return s

arr = [0] * N
for i in range(N):
    arr[i] = int(rnd.random() * 100)
print(mpl(arr),arr)
