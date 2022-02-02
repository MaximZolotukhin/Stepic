"""
7.5 Функции с произвольным числом параметров

Подвиг 3. Объявите функцию с именем get_even, которая принимает произвольное количество
чисел в качестве аргументов и возвращает список, составленный только из четных переданных значений.
Функцию выполнять не нужно, только определить.

Sample Input: 45 4 8 11 12 0
Sample Output: 4 8 12 0
"""

def get_even(*num):
    """
    Функция принимает произвольное количество чисел в качестве аргументов
    и возвращает список, составленный только из четных переданных значений
    :param num: список пользовательских значений
    :return: список четных значений
    """
    return [i for i in num if i % 2 == 0]


num = list(map(int, input().split()))
print(get_even(*num))