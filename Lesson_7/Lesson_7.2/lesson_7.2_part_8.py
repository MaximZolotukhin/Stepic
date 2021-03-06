"""
7.2 Оператор return

Подвиг 8. Объявите функцию, которая принимает строку (в качестве аргумента) и возвращает два значения в виде кортежа:
переданная строка и ее длина.

После объявления функции прочитайте (с помощью функции input) список названий городов, записанных
в одну строку через пробел. Затем, используя генератор словарей и созданную функцию, сформируйте словарь d в формате:

d = {<город 1>: <число символов>, ..., <город N>: <число символов>}

Выведите этот словарь в порядке возрастания длин строк с помощью команд:

a = sorted(d, key=lambda x: d[x])
print(*a)

P. S. Пока просто запишите эти команды. Как они работают станет ясно позже,
когда мы подробнее изучим функции сортировки и работу оператора *.

Sample Input: Воронеж Лондон Тверь Омск Уфа
Sample Output: Уфа Омск Тверь Лондон Воронеж
"""

def len_string(str_1):
    """
    Функция считает количество символов в слове
    :param str_1: Пользовательское слово
    :return: кортеж с слово и его длиной
    """
    result = (str_1, len(str_1))
    return result


str_1 = input().split() # Пользовательский ввод
d = {len_string(val_1)[0]: len_string(val_1)[1] for val_1 in str_1} # Из списка извлекаем одно слово
# и передаем ее в функцию дальше по ключу записываем слово, в значение длину

a = sorted(d, key=lambda x: d[x])
print(*a)
