# 1. Средствами языка Python сформировать два текстовых файла (.txt), содержащих по одной
# последовательности из целых положительных и отрицательных чисел. Сформировать
#  новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую обработку элементов:
# Содержимое первого файла:
# Четные элементы:
# Количество четных элементов:
# Среднее арифметическое:
# Содержимое второго файла:
# Нечетные элементы:
# Количество нечетных элементов:
# Сумма положительных элементов:
a = [4, -6, 5, -7, 9, 3, -2]
b = [3, 8, -4, 5, -1, 9, 7]
c = str(a)[1:-1]
d = str(b)[1:-1]

f1 = open('file_1.txt', 'w+', encoding='UTF-8')
f1.writelines(c)
f1.close()

f2 = open('file_2.txt', 'w+', encoding='UTF-8')
f2.writelines(d)
f2.close()

even = []
odd = []
k1 = 0
k2 = 0

for i in range(len(a)):
    if a[i] % 2 == 0:
        even.append(a[i])
        k1 += 1

for i in range(len(b)):
    if b[i] % 2 != 0:
        odd.append(b[i])
        k2 += 1

f = open('final.txt', 'w')
print('Содержимое первого файла:', open('file_1.txt').read(), file=f)
print('Четные элементы:', *even, file=f)
print('Количество четных элементов:', k1, file=f)
print('Среднее арифметическое:', sum(a)/len(a), '\n', file=f)
print('Содержимое второго файла:', open('file_2.txt').read(), file=f)
print('Нечетные элементы:', *odd, file=f)
print('Количество нечетных элементов:', k2, file=f)
print('Сумма положительных элементов:', sum([i for i in b if i > 0]), file=f)
f.close()






























