"""
4.2 Вложенные условия и множественный выбор

Подвиг 5. Вводится порядковый номер месяца (1, 2, ..., 12).
Вывести на экран количество дней в этом месяце. Принять,
что год не является високосным. Реализовать через условный оператор,
в котором следует использовать не более трех ветвей (блоков).

P.S. Число дней в месяцах не високосного года, начиная с января: 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31

Sample Input: 2
Sample Output: 28
"""

# Сохраняю в переменную номер месяца
number_mounth = int(input())
# Выполняю проверку согласно условию
if number_mounth == 1:
    print('31')
elif number_mounth == 2:
    print('28')
elif number_mounth == 3:
    print('31')
elif number_mounth == 4:
    print('30')
elif number_mounth == 5:
    print('31')
elif number_mounth == 6:
    print('30')
elif number_mounth == 7:
    print('31')
elif number_mounth == 8:
    print('31')
elif number_mounth == 9:
    print('30')
elif number_mounth == 10:
    print('31')
elif number_mounth == 11:
    print('30')
elif number_mounth == 12:
    print('31')

# Можно сократить объединив месяцы с одинаковый количеством дней
#и привязав к проверки советующие номера месяцев через оператор or
