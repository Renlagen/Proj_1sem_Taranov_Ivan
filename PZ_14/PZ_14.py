import re
reg1 = re.compile("\d{3}.\d{3}.\d{3}.[0]")
reg2 = re.compile("\d{3}.\d{3}.\d{3}.\d{3}")
k1, k2 = 0, 0
with open('ip_address.txt', 'r', encoding='utf-8') as source:
    r = source.read()

with open('res1.txt', 'w+', encoding='utf-8') as res1:
    ip0 = re.findall(reg1, r)
    a = res1.write(' \n'.join(map(str, ip0)))
    for i in ip0:
        re.findall('\n', i)
        k1 += 1

with open('res2.txt', 'w', encoding='utf-8') as res2:
    ipall = re.findall(reg2, r)
    res2.write(' \n'.join(map(str, ipall)))
    for i in ipall:
        re.findall('\n', i)
        k2 += 1

print('Количество строк в первом файле:', k1)
print('Количество строк во втором файле:', k2)