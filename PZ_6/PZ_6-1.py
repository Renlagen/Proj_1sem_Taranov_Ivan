# Дан список размера N и целые числа K и L (1 < K ≤ L ≤ N). Найти среднее
# арифметическое всех элементов списка, кроме элементов с номерами от K до L
# включительно
from random import randrange

n = input('Введите целое число N: ')

while type(n) != int:
    try:
        n = int(n)
        if n < 1:
            print('Введено число, которое меньше 1!')
            n = input('Введите целое число N: ')
    except ValueError:
        print('Введено не целое число!')
        n = input('Введите целое число N: ')


l = input("Введите целое число L: ")

while type(l) != int:
    try:
        l = int(l)
        if l > n:
            print('Введено число, которое больше N!')
            l = input('Введите целое число L: ')
    except ValueError:
        print('Введено не целое число!')
        l = input('Введите целое число L: ')


k = input("Введите целое число K: ")

while type(k) != int:
    try:
        k = int(k)
        if k >= l:
            print('Введено число, которое больше L!')
            k = input('Введите целое число K: ')
    except ValueError:
        print('Введено не целое число!')
        k = input('Введите целое число K: ')


tbl = []
sum = 0

for i in range(1, n + 1):
    tbl.append(i)

for i in range(0, k):
    sum += tbl[i]

for i in range(l, n):
    sum += tbl[i]

print('\nРезультат:', sum / (k - 1 + (n - l)))
