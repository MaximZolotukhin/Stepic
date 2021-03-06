"""
7.12 Передача аргументов декораторам

Подвиг 4. Объявите функцию с именем get_list и следующим описанием в теле функции:
'''Функция для формирования списка целых значений'''

Сама функция должна формировать и возвращать список целых чисел, который поступает на ее вход в виде строки
из целых чисел, записанных через пробел.
Определите декоратор, который выполняет суммирование значений из списка этой функции и возвращает результат.
Внутри декоратора декорируйте переданную функцию get_list с помощью команды @wraps (не забудьте сделать импорт:
from functools import wraps). Такое декорирование необходимо, чтобы исходная функция get_list сохраняла
свои локальные свойства: __name__ и __doc__.

Примените декоратор к функции get_list, но не вызывайте ее.
"""
from functools import wraps


def sum_number(start=0): # Функция для передачи параметра в декоратор
    def dec_sun(func): # Декоратор с приемом функция для декорирования
        @wraps(func)
        def wrapper(*args, **kwargs): # Внутренняя функция которая выполняет условие
            perem = func(*args)
            return sum(perem) # складываем сумму из списка и стартовую сумму
        return wrapper
    return dec_sun


@sum_number() # Декоратор с возможность передачи параметра
def get_list(string): # функция переводит строку в список
    """Функция для формирования списка целых значений"""
    list_result = [int(val) for val in string.split()]
    return list_result

s = get_list("1 2 3 -1 -2 -3")
print(s)



# from functools import wraps
#
#
# def dec(func):
#     @wraps(func)
#     def wrapper(args):
#         res = func(args)
#         return sum(res)
#     return wrapper
# @dec
# def get_list(args):
#     args=[int(i) for i in args.split()]
#     '''Функция для формирования списка целых значений'''
#     return args