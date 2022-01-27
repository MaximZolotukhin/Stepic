"""
7.5 Функции с произвольным числом параметров

Значимый подвиг 7. (Для закрепления предыдущего материала). Объявите функцию с именем str_min,
которая сравнивает две переданные строки и возвращает минимальную из них (то есть,
выполняется лексикографическое сравнение строк). Затем, используя функциональный
подход к программированию (то есть, более сложные функции реализуются путем вызова более простых),
реализовать еще две аналогичные функции:

- с именем str_min3 для поиска минимальной строки из трех переданных строк;
- с именем str_min4 для поиска минимальной строки из четырех переданных строк.

Выполнять функции не нужно, только записать.
"""
def str_min(*str):
    """
    Функция возвращает число с минимальным значение
    :param str: Переданные значения
    :return: Возвращаем минимальное значение
    """
    if len(str) == 2:
        str_1, str_2 = str
        if str_1 < str_2:
            return str_1
        else:
            return str_2
    elif len(str) == 3:
        return str_min3(*str)
    elif len(str) == 4:
        return str_min4(*str)


def str_min3(*str):
    str_1, str_2, str_3 = str
    return str_min(str_1, str_min(str_2, str_3))

def str_min4(*str):
    str_1, str_2, str_3, str_4 = str
    return str_min(str_1, str_min(str_2, str_min(str_3, str_4)))


# Не правильное решение
#
# def str_min(*str):
#     if len(str) == 2:
#         str_1, str_2 = str
#         if str_1 < str_2:
#             return str_1
#         else:
#             return str_2
#     elif len(str) == 3:
#         return str_min3(*str)
#     elif len(str) == 4:
#         return str_min4(*str)
#
#
# def str_min3(*str):
#     str_1, str_2, str_3 = str
#     if str_1 < str_2:
#         if str_1 < str_3:
#             return str_1
#     elif str_2 < str_3:
#         if str_1 > str_2:
#             return str_2
#     elif str_1 > str_3:
#         if str_2 > str_3:
#             return str_3
#
#
# def str_min4(*str):
#     str_1, str_2, str_3, str_4 = str
#     if str_1 < str_2 and str_1 < str_3 and str_1 < str_4:
#         return str_1
#     elif str_2 < str_3 and str_2 < str_4:
#         return str_2
#     elif str_3 < str_4:
#         return str_3
#     else:
#         return str_4
#
#
# str = ("Словарь", "Слово", "Жук", "Армия")
#
# print(str_min(*str))