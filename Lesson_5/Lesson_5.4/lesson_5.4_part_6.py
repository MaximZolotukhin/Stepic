"""
5.4 Примеры работы оператора цикла for. Функция enumerate

Подвиг 6. Вводится список в виде вещественных чисел в одну строку через пробел.
С помощью цикла for необходимо найти наименьшее значение в этом списке.
Полученный результат вывести на экран.  Реализовать программу
без использования функции min, max и сортировки.

Sample Input: 8.6 9.11 -4.567 -10.0 1.45
Sample Output: -10.0
"""

numbers_list = list(map(float, input().split())) # Сохраняем в список
number = numbers_list[0] # Сохраняю первое число в переменную

for value in numbers_list: # Сохраняю первое число в переменную
    if number > value:  # Если значение меньше числа то сохраняю его в число
        number = value
    else:
        continue

print(number)