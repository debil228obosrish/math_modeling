from math import sqrt
a = float(input ("введите число a: "))
b = float(input ("введите число b: "))
c = float(input ("введите число c: "))
d = b**2 - 4*a*c
if (d<0):
 print ("Нет корней")
elif (d == 0):
 x = -b/2*a
 print (x)
elif (d > 0):
  x1 = (-b+sqrt(d))/2*a
  x2 = (-b-sqrt(d))/2*a
  print (x1, x2)
