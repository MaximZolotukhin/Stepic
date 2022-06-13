"""
9.7 Аргумент key для сортировки по ключу

Подвиг 2. На вход программы поступает строка в формате:
предмет_1=вес_1
...
предмет_N=вес_N

Веса предметов заданы целыми числами. Необходимо на основе этих данных сформировать словарь и, затем,
на основе этого словаря сформировать список предметов по убыванию их веса.
(В списке должны находиться только наименования предметов без их весов).
Отобразить полученный результат в виде строки с названиями через пробел.
P. S. Для считывания списка целиком в программе уже записаны начальные строчки.

Sample Input:
ножницы=100
котелок=500
спички=20
зажигалка=40
зеркальце=50

Sample Output:
котелок ножницы зеркальце зажигалка спички
"""

import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список строк lst_in)
def dic_in_list(lst_in):
    dict_1 = {lst[0]:int(lst[1]) for lst in [val.split('=') for val in lst_in]}
    return dict_1

d = dic_in_list(lst_in)
res = sorted(d, key=d.get, reverse=True)


print(*res)

# -------------------------- Варина 2 ---------------------------------
dic_lst = {x: int(y) for x, y in [z.split('=') for z in lst_in]}
print(*sorted(dic_lst, key=lambda x: dic_lst[x], reverse=True))