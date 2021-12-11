"""
2.3 Математические функции и модуль math

Подвиг 6. Допишите программу для нахождения числа сочетаний из n по k (значения вводятся в программе),
используя формулу ., где . Выведите результат в консоль в виде целого числа с помощью функции print.
Для вычисления факториалов воспользуйтесь соответствующей функцией из библиотеки math.

Sample Input: 6 3
Sample Output: 20
"""

from math import factorial, trunc # Подключаю библиотеку math

# ввод данных
n, k = map(int, input().split())

# factorial - Факториалом числа называют произведение всех натуральных чисел до него включительно. Например, факториал числа 5 равен произведению 1 * 2 * 3 * 4 * 5 = 120.
# trunc - Функция характеризуется отбрасыванием дробной части. После преобразования получается целое значение без учета дроби.
c = (factorial(n) / (factorial(k) * factorial((n - k)))) # Реализация формулы

print(trunc(c)) # Вывод результата
