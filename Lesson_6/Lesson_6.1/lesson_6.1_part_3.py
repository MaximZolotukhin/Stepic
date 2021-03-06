"""
6.1 Введение в словари

Подвиг 3. Вводятся данные в формате ключ=значение в одну строчку через пробел.
Значениями здесь являются целые числа (см. пример ниже).
Необходимо на их основе создать словарь d с помощью функции dict()
и вывести его на экран командой:
print(*sorted(d.items()))

Sample Input: one=1 two=2 three=3
Sample Output: ('one', 1) ('three', 3) ('two', 2)
"""

dict_1 = dict([value.split('=') for value in input().split()]) # Сохраняем введенную информацию разделяя по пробелам
# так же каждый полученный элемент после ввода разделяем по знаку =

for кey, value in dict_1.items(): # Прохожу по словарю и
    dict_1[кey] = int(value) # преобразую все значения в int

print(*sorted(dict_1.items()))