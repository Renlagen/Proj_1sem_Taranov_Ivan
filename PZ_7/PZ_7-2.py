# Дана строка, состоящая из русских слов, разделенных пробелами (одним или
# несколькими). Найти длину самого длинного слова.

a = input('Введите слова:').split()

c = 0

for i in range(len(a)):
    if len(a[i]) > c:
        c = len(a[i])
        word = a[i]
print('\nСамое длинное слово:', word)
