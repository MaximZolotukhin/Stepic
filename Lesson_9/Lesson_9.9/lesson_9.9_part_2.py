"""
9.9 Функции all и any

Подвиг 1. Вводится строка целых чисел через пробел. Необходимо определить, являются ли все эти числа четными.
Вывести True, если это так и False - в противном случае.
Задачу реализовать с использованием одной из функций: any или all.

Sample Input:
2 4 6 8 22 56
2 4 6 8 22 56 11

Sample Output:
True
"""

lst_in = list(map(int, input().split()))

lst_out = []
for x in lst_in:
    if x % 2 == 0:
        lst_out.append(True)
    else:
        lst_out.append(False)

print(all(lst_out))

#----------------- Вариант 2 ------------------

lst_in = list(map(int, input().split()))
lst_out_2 = [True if y % 2 == 0 else False for y in lst_in]
print(all(lst_out_2))

