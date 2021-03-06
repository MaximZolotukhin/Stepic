"""
5.2 Операторы break, continue и else

Подвиг 7. Вводится натуральное число n. Вывести первое найденное натуральное число
(то есть, перебирать числа, начиная с 1), квадрат которого больше значения n.
Реализовать программу с использованием цикла while.

Sample Input: 10
Sample Output: 4
"""

num = int(input()) # Пользовательский ввод информации
count = 1 # Счетчик

while True:
    if num < count**2: # Если число меньше квадрата счетчика
        print(count) # Выводим результат и прерываем работу цикла
        break
    else: # Иначе увеличиваем счетчик на 1
        count += 1
