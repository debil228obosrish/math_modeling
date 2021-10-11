a = int(input("Введите первое число:"))
b = int(input("Введите второе число:"))
h = int(input("Введите член геометрической прогрессии:"))

c = [a * b ** (n-1) for n in range(1, h + 1)]
print(c)