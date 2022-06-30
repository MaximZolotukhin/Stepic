"""
10.3 Модуль random стандартной библиотеки

Подвиг 5. Вводится таблица целых чисел, записанных через пробел. Необходимо перемешать
столбцы этой таблицы, используя функции shuffle и zip и вывести результат на экран (также в виде таблицы).

P. S. Для считывания списка целиком в программе уже записаны начальные строчки.

Sample Input:
1 2 3 4
5 6 7 8
9 8 6 7

Sample Output:
4 1 3 2
8 5 7 6
7 9 6 8
"""
import sys
import random
# установка "зерна" датчика случайных чисел, чтобы получались одни и те же случайные величины

random.seed(1)

# считывание списка из входного потока получаем ['1 2 3 4', '5 6 7 8', '9 8 6 7']
lst_in = list(map(str.strip, sys.stdin.readlines()))
# print(lst_in)
# Преобразовываем в думерный список состоящий из целочисленных значений получаем [[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 6, 7]]
list_mid = [list(map(int, x.split())) for x in lst_in]
# print(list_mid)
# Разбераем наш массив получаем [(1, 5, 9), (2, 6, 8), (3, 7, 6), (4, 8, 7)]
list_mid_1 = list(zip(*list_mid))
# print(list_mid_1)
# перемешиваем наш массив получаем [(4, 8, 7), (1, 5, 9), (3, 7, 6), (2, 6, 8)]
random.shuffle(list_mid_1)
# print(list_mid_1)
# Разбераем наш массив получаем [(4, 1, 3, 2), (8, 5, 7, 6), (7, 9, 6, 8)]
list_mid_2 = zip(*list_mid_1)

for val in list_mid_2:
    print(*val)
