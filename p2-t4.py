a=int(input("введите делимое"))
b=int(input("введите делитель"))
if b == 0:
  print("лох")

elif a % b == 0:
  print(a/b, "ОСТАТКА НЕТ")
elif a % b != 0:
  print(a/b, "ОСТАТОК ЕСТЬ:", a%b )