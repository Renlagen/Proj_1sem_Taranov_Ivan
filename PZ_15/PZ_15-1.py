# В матрице найти минимальный элемент в предпоследнем столбце.
import random
import numpy as np
i, j = int(input('Введите количество строк: ')), int(input('Введите количество столбцов: '))
o = i * j
matrix = np.array([random.randint(-5, 5) for k in range(o)])
matrix.shape = (i, j)
print('\nИсходная матрица:\n', matrix)
tet = np.min(matrix[:, -2])
print('\nМинимальный элемент в предпоследнем столбце: {}'.format(tet))