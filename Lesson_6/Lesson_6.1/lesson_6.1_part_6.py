"""
6.1 Введение в словари

Подвиг 6. Вводятся данные в формате ключ=значение в одну строчку через пробел.
Необходимо на их основе создать словарь d, затем удалить из этого словаря ключи
'False' и '3', если они существуют. Ключами и значениями словаря являются строки.
Вывести полученный словарь на экран командой:

print(*sorted(d.items()))

Sample Input: лена=имя дон=река москва=город False=ложь 3=удовлетворительно True=истина
Sample Output: ('True', 'истина') ('дон', 'река') ('лена', 'имя') ('москва', 'город')
"""

dict_1 = dict([value.split('=') for value in input().split()]) # Сохраняем введенную информацию разделяя по пробелам
# так же каждый полученный элемент после ввода разделяем по знаку =

if 'False' in dict_1: # Проверяю наличие значение в словаре
    del dict_1['False'] # Удаляю их по ключу
if '3' in dict_1:
    del dict_1['3']

print(*sorted(dict_1.items())) # Вывожу результат