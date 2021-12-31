"""
5.6 Вложенные циклы

Подвиг 2. Вводится список из URL-адресов (каждый с новой строки).
Требуется в них заменить все пробелы на символ дефиса (-). Следует учесть,
что может быть несколько подряд идущих пробелов. Результат преобразования
вывести на экран в виде строк из URL-адресов.

P. S. Для считывания списка целиком в программе уже записаны начальные строчки.

Sample Input:
django chto  eto takoe    poryadok ustanovki
model mtv   marshrutizaciya funkcii  predstavleniya
marshrutizaciya  obrabotka isklyucheniy       zaprosov perenapravleniya

Sample Output:
django-chto-eto-takoe-poryadok-ustanovki
model-mtv-marshrutizaciya-funkcii-predstavleniya
marshrutizaciya-obrabotka-isklyucheniy-zaprosov-perenapravleniya
"""

import sys
# lst_in = ['django chto  eto takoe    poryadok ustanovki', 'model mtv   marshrutizaciya funkcii  predstavleniya', 'marshrutizaciya  obrabotka isklyucheniy       zaprosov perenapravleniya' ]

# Cчитывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)
for string_word in lst_in: # Перебираю позиции в списке
    while '  ' in string_word: # Прохожу циклом пока в строке встречается двойной пробел
        string_word = string_word.replace('  ', ' ') # Заменяю двойные пробелы на одинарные
    print(string_word.replace(' ','-'))# Вывожу результат заменяя все пробел на -
