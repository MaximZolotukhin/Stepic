"""
5.3 Оператор цикла for и функция range

Подвиг 8. Вводится натуральное число n. С помощью цикла for определить,
является ли оно простым (то есть, делится нацело только на само себя и на 1).
Вывести на экран ДА, если n простое и НЕТ - в противном случае.

Sample Input: 11
Sample Output: ДА
"""

user_number = int(input()) # Пользовательский ввод
flag = True # флаг устанавливаем в значение True

for i in range(2, user_number // 2+1): # Чтобы не перебирать все число мы может получить остаток от деления + 1
    if (user_number % i == 0): # Если остаток от деления равен 0
        flag = False # меняем значение флага на False
# Если флаг True выводим ДА
if (flag):
    print("ДА")
else: # Иначе НЕТ
    print("НЕТ")
