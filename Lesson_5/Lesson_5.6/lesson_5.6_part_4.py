"""
5.6 Вложенные циклы


Подвиг 4. Вводится двумерный список размерностью 5 х 5 элементов, состоящий из нулей и,
в некоторых позициях, единиц (см. пример ввода ниже). Требуется проверить,
не касаются ли единицы друг друга по горизонтали, вертикали и диагонали.
То есть, вокруг каждой единицы должны быть нули. Если проверка проходит вывести ДА, иначе - НЕТ.

P. S. Для считывания списка целиком в программе уже записаны начальные строчки.

Sample Input:
1 0 0 0 0
0 0 1 0 1
0 0 0 0 0
0 1 0 1 0
0 0 0 0 0

Sample Output: ДА
"""

import sys

lst_in = [
    [1, 1, 0, 0, 0],
    [0, 0, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0]
]

# считывание списка из входного потока
# s = sys.stdin.readlines()
# lst_in = [list(map(int, x.strip().split())) for x in s]

# здесь продолжайте программу (используйте список lst_in)
string_matrix = len(lst_in[0])
flag = True

lst_in = [[0]*string_matrix] + (lst_in) + [[0]*string_matrix] # Добавляем строки вверх и вниз матрицы
for i in range(len(lst_in)): # Добавляем столбцы
    lst_in[i].insert(0, 0) # Первый столбец матрицы
    lst_in[i].append(0) # Последний столбец матрицы

for index_str, value in enumerate(lst_in): # Прохожу по строкам и сохраняю данные в переменную value, индексы index_str
    if flag == True: # Ставлю флаг в True
        for index_positon, value_str in enumerate(value): # Ставлю флаг в True
            if value_str == 1: # Если встречаю 1 в матрице начинаю проверять на соприкосновение с другими единицами
                if (lst_in[index_str][index_positon + 1] == 1 or lst_in[index_str][index_positon - 1] == 1):# Слева или справа
                    flag = False
                    break
                if 1 in lst_in[index_str - 1][index_positon - 1: index_positon +1]: # Верхний ряд
                    flag = False
                    break
                if 1 in lst_in[index_str + 1][index_positon - 1: index_positon +1]: # Нижний ряд
                    flag = False
                    break
                    # Случае нахождения прерываю поиск, flag ставлю в False
                else:
                    flag = True # Иначе flag = True
    else:
        break  # Если флаг в положение False прерываю поиск.


if flag:
    print("ДА")
else:
    print("НЕТ")
