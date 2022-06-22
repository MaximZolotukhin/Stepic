"""
9.9 Функции all и any

Подвиг 4. Вводятся оценки студента в одну строчку через пробел. Необходимо определить,
имеется ли в этом списке хотя бы одна оценка ниже тройки. Если это так, то вывести на
экран строку "отчислен", иначе - "учится".
Задачу реализовать с использованием одной из функций: any или all.

Sample Input:
3 3 3 2 3 3

Sample Output:
отчислен
"""

lst_in = list(map(int, input().split()))
lst_out_2 = [False if y < 3 else True for y in lst_in]
print('учится' if all(lst_out_2) else 'отчислен')

# Решение варинат 2

print(['учится', 'отчислен'][any(map(lambda x: int(x) < 3, input().split()))])

# Решение варинат 3
print('учится' if all(map(lambda x: x >= 3, map(int, input().split()))) else 'отчислен')
