"""
4.2 Вложенные условия и множественный выбор

Подвиг 6. Дата некоторого дня характеризуется двумя натуральными числами: m (порядковый номер месяца) и n (число).
По введенным m и n (в одну строку через пробел) определить:

а) дату предыдущего дня (принять, что m и n не характеризуют 1 января);
б) дату следующего дня (принять, что m и n не характеризуют 31 декабря).

В задаче принять, что год не является високосным. Вывести предыдущую дату и следующую дату
(в формате: mm.dd, где m - число месяца; d - номер дня) в одну строчку через пробел.
P.S. Число дней в месяцах не високосного года, начиная с января: 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31

Sample Input: 8 31
Sample Output: 08.30 09.01
"""
number_mounth, day = map(int, input().split())
day_31 = (1, 3, 5, 7, 8, 10, 12)
day_30 = (4, 6, 9, 11)

# Февраль 28 ---------------------------------------------------------------
if number_mounth == 2:
    if day == 1:
        day_1, mounth_1 = 28, 1
        print(f'0{mounth_1}.{day_1+3} 0{number_mounth}.0{day + 1}')
    elif day == 28:
        day_1, mounth_1 = 28, '02'
        day_2 = '01'
        print(f"{mounth_1}.{day_1-1} 0{number_mounth+1}.{'01'}")
    elif day > 28:
        print(f'в месяце всего 28 дней')
    else:
        day_2 = day + 1
        print(f"{str(number_mounth).rjust(2, '0')}.{str(day - 1).rjust(2, '0')} {str(number_mounth).rjust(2, '0')}.{str(day_2).rjust(2, '0')}")

# Апрель 4, Июнь 6, Сентябрь 9, Ноября 11 ---------------------------------------
elif number_mounth in day_30:
    if day == 1:
        day_1, mounth_1 = 31, number_mounth - 1
        day_2 = day + 1
        print(f"{str(mounth_1).rjust(2, '0')}.{str(day_1).rjust(2, '0')} {str(number_mounth).rjust(2, '0')}.{str(day_2).rjust(2, '0')}")
    elif day == 30:
        day_1, mounth_1 = 29, number_mounth
        day_2 = 1
        print(f"{str(mounth_1).rjust(2, '0')}.{str(day_1).rjust(2, '0')} {str(number_mounth + 1).rjust(2, '0')}.{str(day_2).rjust(2, '0')}")
    elif day > 30:
        print(f'в месяце всего 30 день')
    else:
        day_2 = day + 1
        print(f"{str(number_mounth).rjust(2, '0')}.{str(day-1).rjust(2, '0')} {str(number_mounth).rjust(2, '0')}.{str(day_2).rjust(2, '0')}")

#Январь 1   Март 3   Май 5   Июль 7   Август 8   Октябрь 10   Декабрь 12 --------------------------------------------------------------
elif number_mounth in day_31:
    if day == 1:
        day_1, mounth_1 = 30, number_mounth - 1
        day_2 = day + 1
        if number_mounth == 3:
            print(f"{str(mounth_1).rjust(2,'0')}.28 {str(number_mounth).rjust(2,'0')}.{str(day_2).rjust(2,'0')}")
        elif number_mounth == 1:
            print(f"{str(12).rjust(2, '0')}.{31} 0{number_mounth}.0{day_2}")
        else:
            print(f"{str(mounth_1).rjust(2,'0')}.{str(day_1).rjust(2,'0')} {str(number_mounth).rjust(2,'0')}.{str(day_2).rjust(2,'0')}")
    elif day == 31:
        day_1, mounth_1 = 30, number_mounth
        day_2 = 1
        if number_mounth == 12:
            print(f'{mounth_1}.{day_1} 01.0{day_2}')
        else:
            print(f"{str(mounth_1).rjust(2, '0')}.{str(day_1).rjust(2, '0')} {str(number_mounth + 1).rjust(2, '0')}.{str(day_2).rjust(2, '0')}")
    elif day > 31:
        print(f'в месяце всего 31 день')
    else:
        day_2 = day + 1
        print(f"{str(number_mounth).rjust(2, '0')}.{str(day - 1).rjust(2, '0')} {str(number_mounth).rjust(2, '0')}.{str(day_2).rjust(2, '0')}")
