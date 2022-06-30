"""
7.5 Функции с произвольным числом параметров

Большой подвиг 6. (Для закрепления предыдущего материала). Вводится таблица целых чисел (см. пример ниже)
размером N x N элементов (N определяется по входным данным). Эта таблица содержит нули, но кое-где - единицы.
С помощью функции с именем verify, на вход которой передается двумерный список чисел, необходимо проверить,
являются ли единицы изолированными друг от друга, то есть, вокруг каждой единицы должны быть нули.

Рекомендуется следующий алгоритм. В функции verify производить перебор двумерного списка.
Для каждого элемента (списка) со значением 1 вызывать еще одну вспомогательную функцию is_isolate
для проверки изолированности единицы. То есть, функция is_isolate должна возвращать True,
если единица изолирована и False - в противном случае.

Как только встречается не изолированная единица, функция verify должна возвращать False.
Если успешно доходим (по элементам списка) до конца, то возвращается значение True.

Функцию выполнять не нужно, только определить.

P. S. При реализации функции is_isolate не следует прописывать восемь операторов if.
Подумайте, как это можно сделать красивее (с точки зрения реализации алгоритма).

Sample Input:
1 0 0 0 0
0 0 1 0 0
0 0 0 0 0
0 1 0 1 0
0 0 0 0 0

Sample Output: True
# """
#
# def verify(*matrix):
#     # здесь продолжайте программу (используйте список lst_in)
#     flag = True
#     for index_out, val_out in enumerate(matrix): # Вытаскиваем вложенные списки, index_out нужен для построения матрицы на передачу
#         for index, val in enumerate(val_out): # проходем по вложенному списку, index нужен для построения матрицы на передачу
#             if val == 1:
#                 result = is_isolate(*matrix)
#                 if result:
#                     flag = False
#                     break
#                 else:
#                     flag = True
#     return flag
#
#
# def is_isolate(*matrix):
#     """
#     То есть, функция is_isolate должна возвращать True,
#     если единица изолирована и False - в противном случае.
#     :param matrix:
#     :return:
#     """
#     list_in = list(matrix[:]) # Делаю дубликат в виде списка
#     string_matrix = len(list_in[0]) # Узнаю длину списка
#     flag = True
#
#     lst_in = [[0] * string_matrix] + (list_in) + [[0] * string_matrix]  # Добавляем строки вверх и вниз матрицы
#     for i in range(len(list_in)):  # Добавляем столбцы
#         lst_in[i].insert(0, 0)  # Первый столбец матрицы
#         lst_in[i].append(0)  # Последний столбец матрицы
#
#     for index_str, value in enumerate(list_in):  # Прохожу по строкам и сохраняю данные в переменную value, индексы index_str
#         if flag == True:  # Ставлю флаг в True
#             for index_positon, value_str in enumerate(value):  # Ставлю флаг в True
#                 if value_str == 1:  # Если встречаю 1 в матрице начинаю проверять на соприкосновение с другими единицами
#                     if (list_in[index_str][index_positon + 1] == 1 or list_in[index_str][
#                         index_positon - 1] == 1):  # Слева или справа
#                         flag = True
#                         break
#                     if 1 in list_in[index_str - 1][index_positon - 1: index_positon + 1]:  # Верхний ряд
#                         flag = True
#                         break
#                     if 1 in list_in[index_str + 1][index_positon - 1: index_positon + 1]:  # Нижний ряд
#                         flag = True
#                         break
#                         # Случае нахождения прерываю поиск, flag ставлю в False
#                     else:
#                         flag = False  # Иначе flag = True
#         else:
#             break  # Если флаг в положение False прерываю поиск.
#
#     return flag
#
#
# matrix = [[1, 0, 0, 0, 0],
#            [0, 0, 1, 0, 0],
#            [0, 0, 0, 0, 0],
#            [0, 1, 0, 1, 0],
#            [0, 0, 0, 0, 0]
# ]
#
# print(verify(*matrix))

# --------------------------------------------------------------------------------------------------------------
def is_isolate(lst):
    if sum(lst) == 1:
        return True
    else:
        return False


def verify(args):
    lst_in = args
    N = int(len(lst_in[1]))

    lst_in.insert(0, [0] * N)
    lst_in.insert(N + 1, [0] * N)

    for v in lst_in:
        v.insert(0, 0)
        v.insert(N + 1, 0)

    r = []
    s = 0
    for row in range(1, len(lst_in) - 1):
        for col in range(1, len(lst_in[row]) - 1):
            if lst_in[row][col] == 1:
                r.append(lst_in[row - 1][col - 1])
                r.append(lst_in[row - 1][col])
                r.append(lst_in[row - 1][col + 1])
                r.append(lst_in[row][col - 1])
                r.append(lst_in[row][col + 1])
                r.append(lst_in[row][col])
                r.append(lst_in[row + 1][col + 1])
                r.append(lst_in[row + 1][col])
                r.append(lst_in[row + 1][col - 1])
                if is_isolate(r):
                    s += 0
                else:
                    s += 1
                r = []

    return True if s == 0 else False