"""
9.1 Выражения-генераторы

Подвиг 6. Вводится целое положительное число a. Необходимо определить генератор,
который бы возвращал модули чисел в диапазоне [-a; a], а затем еще один,
который бы вычислял кубы чисел (возведение в степень 3), возвращаемых первым генератором.

Вывести в одну строчку через пробел первые четыре значения. (Полагается,
что генератор выдает, как минимум четыре значения).

Sample Input: 3
Sample Output: 27 8 1 0
"""

# ввод значений a и b (переменные a и b не менять!)
a = int(input())

# здесь продолжайте программу
gen = (abs(num) for num in range(-a, a)) # Выражение генератор возвращает модуль числа
gen_2 = (num**3 for num in gen) # Выражение генератор число в 3 степени

for i in range(0, 4):
    print(next(gen_2), end=' ')
