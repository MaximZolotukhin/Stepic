"""
4.2 Вложенные условия и множественный выбор

Подвиг 4. Вводится порядковый номер дня недели (1, 2, ..., 7).
Вывести на экран его название (понедельник, вторник, среда, четверг,
пятница, суббота, воскресенье). Программу реализовать с использованием операторов if-elif.

Sample Input: 2
Sample Output: вторник
"""

# Сохраняю число в переменную
number_day = int(input())
# Сравниваю число и вывожу подходящий результат
if number_day == 1:
    print('понедельник')
elif number_day == 2:
    print('вторник')
elif number_day == 3:
    print('среда')
elif number_day == 4:
    print('четверг')
elif number_day == 5:
    print('пятница')
elif number_day == 6:
    print('суббота')
elif number_day == 7:
    print('воскресенье')