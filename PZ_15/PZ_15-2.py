# Для каждой строки матрицы с нечетным номером найти среднее арифметическое ее элементов
import random
import numpy as np
i, j = int(input('Введите количество строк: ')), int(input('Введите количество столбцов: '))
o = i * j
matrix = np.array([random.randint(-5, 5) for k in range(o)])
matrix.shape = (i, j)
print('\nИсходная матрица:\n', matrix)
print('\nСреднее арифметическое для каждой нечетной строки:')
print(*('({}) = {}'.format(i, sum(i)/len(i)) for i in matrix[::2]), sep='\n')
