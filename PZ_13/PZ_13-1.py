# 1.Даны текущие оценки студента по дисциплине «Основы программирования» за
# месяц. Необходимо найти количество «2», «3», «4» и «5», полученных студентом, и
# определить итоговую оценку за месяц
r = [5, 5, 4, 3, 4, 5, 3, 5, 4, 2, 4, 5, 3, 2, 4]

print('Количество двоек:', len(list(filter(lambda x: x == 2, r))))
print('Количество троек:', len(list(filter(lambda x: x == 3, r))))
print('Количество четверок:', len(list(filter(lambda x: x == 4, r))))
print('Количество пятерок:', len(list(filter(lambda x: x == 5, r))))
print('Итоговая оценка за месяц:', round(sum(r)/len(r)))
