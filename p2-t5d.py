a = int(input('Введите число:'))

for a in range(2,a + 1):
    s = 0
    for b in range(1, int(a // 2)+ 1):
        if a % b == 0:
            s += b
    if s == a:
        print(a)