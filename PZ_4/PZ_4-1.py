# Дано вещественное число X (|X|<1) и целое число N (>0). Найти значение выражения X -
# X3/3 + X5/5 - ... + (-1)NX2N +1/(2N +1). Полученное число является приближенным значением
# функции arctg в точке X.
import math
x = float(input('Введите число x: '))
# Проверка исключений
while type(x) != float:
    try:
        x = float(x)
    except ValueError:
        print("Введите снова!")
        x = input("Введите вещественное число: ")
while abs(x) >= 1:
    x = input("Введите число меньше единицы по модулю: ")
    while type(x) != float:
        try:
            x = float(x)
        except ValueError:
            print("Введите снова!")
            x = input("Введите вещественное число: ")

n = input("Введите целое число n: ")
# Проверка исключений
while type(n) != int:
    try:
        n = int(n)
    except ValueError:
        print("Введите снова!")
        n = input("Введите целое число: ")
while n <= 0:
    n = input("Введите положительное число: ")
    while type(n) != int:
        try:
            n = int(n)
        except ValueError:
            print("Введите снова!")
            n = input("Введите целое число: ")

d1 = 1
R = 0
while d1 < int(n):
    d2 = (-1) ** d1
    d3 = abs(x) ** (2 * d1 + 1) / (2 * d1 + 1)
    d4 = d2 * d3
    R += d4
    d1 += 1
print("\nЗначение выражения равно:", R)
print("Приближенное значение функции arctg в точке x равно:", math.atan(abs(x)))

