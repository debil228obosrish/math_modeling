a = int(input("Введите число a:"))
b = int(input("Введите число b:"))
c = int(input("Введите число c:"))
if (a < b + c) and (b < a + c) and (c < a + b):
  print ("треугольник существует")
  if (a == b) and (b == c):
    print ("треугольник равносторонний")
  elif (a == b) or (b == c) or ( a==c):
    print ("треугольник равнобедренный") 
  else:
    print ("треугольник разносторонний")
else: 
  print ("треугольник не существует")
