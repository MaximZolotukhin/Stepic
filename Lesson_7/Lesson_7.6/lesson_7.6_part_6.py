"""
7.6 Операторы упаковки и распаковки коллекций

Подвиг 6. Имеется словарь, содержащий пункты меню:
menu = {'Главная': 'home', 'Архив': 'archive', 'Новости': 'news'}
Дополнительно вводятся еще пункты меню в виде строк в формате:

название_1=url_1
...
название_N=url_N

Необходимо эту введенную информацию преобразовать в словарь и добавить к словарю menu,
используя оператор распаковки для словарей. На результирующий словарь должна вести переменная menu.
Выводить словарь не нужно, только сформировать.

P. S. Для считывания списка целиком в программе уже записаны начальные строчки.

Sample Input:
Города=about-cities
Машины=read-of-cars
Самолеты=airplanes

Sample Output:
Архив Главная Города Машины Новости Самолеты
about-cities airplanes archive home news read-of-cars
"""
import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))
# Начальный словарь
menu = {'Главная': 'home', 'Архив': 'archive', 'Новости': 'news'}

# dict_test = dict()
# dict_test = dict({key: value for key, value in input().split('=')})

for val in lst_in:  # Извлекаем значения по одному из полученного списка
    # Далее через генератор словарей мы каждое значение помещаем разделяем по знаку равенства (=) и помещаем два
    # значения в список.
    # далее мы каждое значение из полученного списка после разделения присваиваем к двум переменным, их в свою очередь
    # добавляем в ключ и значение словаря полученного генератором словарей,
    # с помощью метода .update() я добавляю значения в начальный словарь
    menu.update({key: value for key, value in [val.split('=')]})

# Вывожу в консоль ключи .keys() и значения .values()
print(*menu.keys())
print(*menu.values())

# menu.update({key: value for key, value in [input().split('=')]})
# menu.update({key: value for key, value in [input().split('=')]})
# menu.update({key: value for key, value in [input().split('=')]})