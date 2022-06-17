"""
9.8 Функция isinstance для проверки типов данных

Подвиг 2. Определите функцию с именем get_add, которая складывает или два числа или две строки
(но не число со строкой) и возвращает полученный результат. Если сложение не может быть выполнено,
то функция возвращает значение None. Сигнатура функции должна быть, следующей:

def get_add(a, b): ...

Вызывать функцию не нужно, только определить. Также ничего не нужно выводить на экран.

P. S. Не забудьте про необходимость различения булевых значений (False, True) от целочисленных.
"""

# a = input()
# b = input()


def get_add(a, b):
    try:
        isinstance(a, (int, float))
        isinstance(b, (int, float))
        if isinstance(a, (bool)) or isinstance(b, (bool)):
            return None
        return a + b
    except TypeError:
        try:
            isinstance(a, (str))
            isinstance(b, (str))
            return a + b
        except TypeError:
            return None

#Решение №2
def get_add_2(a, b):
    if isinstance(a, (bool)) and  isinstance(b, (bool)):
        return a + b
    elif isinstance(a, (str)) and  isinstance(b, (str)):
        return a + b    #
    elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return None
    else:
        return None

if __name__ == "__main__":
    print(get_add(2, 20))
    print(get_add('20', '2'))
    print(get_add('2', 2))
    print(get_add(2, '2'))
    print(get_add(False, '2'))
    print(get_add(3, True))
    print('-'*100)
    print(get_add_2(1, 10))
    print(get_add_2('1', '10'))
    print(get_add_2('1', 10))
    print(get_add_2(1, '10'))
    print(get_add_2(True, 10))
