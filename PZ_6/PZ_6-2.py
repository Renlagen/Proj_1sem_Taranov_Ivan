# Даны списки A и B одинакового размера N. Поменять местами их содержимое и
# вывести вначале элементы преобразованного списка A, а затем — элементы
# преобразованного списка B.
from random import randrange

n = int(input('Введите целое число N: '))

tblA = []
tblB = []

for _ in range(n):
    tblA.append(randrange(1, 100))

for _ in range(n):
    tblB.append(randrange(1, 100))

print('\nСписок A: ', tblA)
print('Список B: ', tblB)

tblA, tblB = tblB, tblA

print('Смена местами значений')
print('Список A: ', tblA)
print('Список B: ', tblB)

