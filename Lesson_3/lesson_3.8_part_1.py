"""
3.8 Методы списков

Подвиг 2. Вводится строка из целых чисел через пробел. Если первое число не равно последнему,
то нужно добавить значение True, а иначе - значение False. Результирующий список lst вывести на экран командой:
print(*lst)
Реализовать задачу без использования условных операторов.

Sample Input: 8 12 2 -10 6
Sample Output: 8 12 2 -10 6 True
"""

# Сохраняем данные в переменную
lst = list(map(int, input().split()))
# Если первое число не равно последнему, то нужно добавить значение True, а иначе - значение False.
lst.append(lst[0]!=lst[-1])
# Выводим результат
print(*lst)
