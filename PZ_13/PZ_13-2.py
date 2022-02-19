# 2.Из заданной строки отобразить только символы пунктуации. Использовать библиотеку string.
# Строка: --msg-template="$FileDir$\{path}:{line}:{column}:{C}:({symbol}){msg}"
import string

a = '--msg-template="$FileDir$\{path}:{line}:{column}:{C}:({symbol}){msg}"'
b = [i for i in a if i in string.punctuation]
print('Результат:', *b)