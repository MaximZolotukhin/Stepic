"""
7.2 Оператор return

Подвиг 3. Объявите функцию с именем is_large, которая принимает строку (в качестве аргумента) и возвращает False,
если длина строки меньше трех символов. Иначе возвращается значение True.
Вызывать функцию не нужно, только объявить.

Sample Input: Я люблю Python!
Sample Output: True
"""

def is_large(str_1):
    """
     Функция проверяет длину строки.

     :param num_1: сторона 1
     :param num_2: сторона 2
     :param num_3: сторона 3
     :return: Если длина строки меньше 3 символов то возвращаю False иначе True
     """
    flag = True
    if len(str_1) < 4:
        flag = False
    else:
        flag = True

    return flag
