number = int(input("Введіть число для таблиці множення: "))
d = int(input("Введіть діапазон чисел (до якого числа): "))

for i in range(1, d+1):
    print(f"{number} x {i} = {number * i}")


