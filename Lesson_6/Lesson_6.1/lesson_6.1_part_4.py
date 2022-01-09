"""
6.1 Введение в словари

Подвиг 4. На вход программы поступают данные в виде набора строк в формате:
ключ1=значение1
ключ2=значение2
...
ключN=значениеN
Ключами здесь выступают целые числа (см. пример ниже). Необходимо их преобразовать в словарь
d (без использования функции dict()) и вывести его на экран командой:

print(*sorted(d.items()))
P. S. Для считывания списка целиком в программе уже записаны начальные строчки.

Sample Input:
5=отлично
4=хорошо
3=удовлетворительно

Sample Output:
(3, 'удовлетворительно') (4, 'хорошо') (5, 'отлично')
"""

import sys
#
# считывание списка из входного потока
list_in = list(map(str.strip, sys.stdin.readlines()))
#
# здесь продолжайте программу (используйте список lst_in)
# list_in = "5=отлично 4=хорошо 3=удовлетворительно"

list_in = [value.split('=') for value in list_in]# Сохраняем введенную информацию разделяя
# каждый полученный элемент после ввода разделяем по знаку =

dict_1 = {} # Создаю пустой словарь
#----------------------------------------------------------------------------
# Пример формирования двумерного списка с изменением знанчения
#lst = [[int(i.split('=')[0]), i.split('=')[1]] for i in list_in]
#----------------------------------------------------------------------------
for i in range(len(list_in)): # Прохожу по списку
    dict_1[int(list_in[i][0])] = list_in[i][1] # Сохраню ключ значение в словарь преобразовывая значения ключи в тип int

print(*sorted(dict_1.items()))
