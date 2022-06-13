"""
9.3 Функция map

Подвиг 6. Вводятся названия городов в одну строчку через пробел. Необходимо определить функцию map,
которая бы возвращала названия городов только длиной более 5 символов. Вместо остальных названий -
строку с дефисом ("-"). Сформировать список из полученных значений и отобразить его на экране в одну
строчку через пробел.

Sample Input: Москва Уфа Вологда Тула Владивосток Хабаровск
Sample Output: Москва - Вологда - Владивосток Хабаровск
"""
str_in = list(input().split())


def len_city(str_in):
    name = str_in
    if len(name) < 5:
        name = '-'
        return name
    else:
        return name

# str_out = list(map(len_city, str_in))
str_out = map(lambda name: '-' if len(name) < 5 else name, str_in)


print(*str_out)