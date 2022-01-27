"""
7.4 Именованные аргументы. Фактические и формальные параметры

Подвиг 6. Функции из предыдущего подвига 5 добавьте еще один формальный параметр up с начальным булевым значением True.
 параметр up равен True, то тег (указанный в формальном параметре tag) следует записывать заглавными буквами,
 а иначе - малыми.

После объявления функции прочитайте (с помощью функции input) строку и дважды вызовите функцию
(с выводом результата ее работы на экран):

- первый раз со строкой и именованным аргументом tag со значением 'div'
- второй раз со строкой, именованным аргументом tag со значением 'div' и именованным аргументом up со значением False.

Sample Input: Python is best!
Sample Output:
<DIV>Python is best!</DIV>
<div>Python is best!</div>
"""

def html_code(string_user, tag='h1', up=True):
    """
    Функция возвращает строку в виде <div>Python is best!</div>
    :param string_user: Пользовательская строк
    :param tag: html тэг
    :param up: Если True то возвращаем с большой буквы, иначе с маленькой
    :return: Возвращаем результат
    """
    if up:
        tag = tag.upper() # Если True тогда перевожу буквы в верхний регистр.
        return f'<{tag}>{string_user}</{tag}>'
    else:
        return f'<{tag}>{string_user}</{tag}>'


string_user = input()
print(html_code(string_user, tag='div'))
print(html_code(string_user, 'div', False))
