# Описать функцию Mean(X, Y, AMean, GMean), вычисляющую среднее арифметическое
# AMean = (X+Y)/2 и среднее геометрическое GMean = y/X Y двух положительных чисел X и
# Y (X и Y — входные, AMean и GMean — выходные параметры вещественного типа). С
# помощью этой функции найти среднее арифметическое и среднее геометрическое для пар
# (A, B), (A, C), (A, D), если даны A, B, C, D.

import math


def AMean(X, Y):
    return (X + Y) / 2


def GMean(X, Y):
    return math.sqrt(X * Y)


print('A: ')
A = float(input())
print('B: ')
B = float(input())
print('C: ')
C = float(input())
print('D: ')
D = float(input())

print('AMean(A, B):', AMean(A, B), ' ', 'GMean(A, B):', GMean(A, B))

print('AMean(A, C):', AMean(A, C), ' ', 'GMean(A, C):', GMean(A, C))

print('AMean(A, D):', AMean(A, D), ' ', 'GMean(A, D):', GMean(A, D))