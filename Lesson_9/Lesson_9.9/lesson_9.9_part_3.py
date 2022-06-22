"""
9.9 Функции all и any

Подвиг 2. Вводится строка вещественных чисел через пробел. Необходимо определить, есть ли среди них хотя
бы одно отрицательное. Вывести True, если это так и False - в противном случае.
Задачу реализовать с использованием одной из функций: any или all.

Sample Input:
8.2 -11.0 20 3.4 -1.2

Sample Output:
True
"""

lst_in = list(map(float, input().split()))
lst_out_2 = [True if y < 0 else False for y in lst_in]
print(any(lst_out_2))
