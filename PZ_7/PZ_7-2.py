# Дана строка, состоящая из русских слов, разделенных пробелами (одним или
# несколькими). Найти длину самого длинного слова.

s = input('Введите слова: ')
word = ''
maxLen = 0
maxWord = ''
for c in s + ' ':
    if c == ' ':
        if len(word) > maxLen:
            maxWord = word
        word = ''
    else:
        word += c
print("\nСамое длинное слово:", maxWord)
