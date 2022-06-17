"""
9.8 Функция isinstance для проверки типов данных

Подвиг 4. Определите функцию с именем get_even_sum, которая принимает на входе итерируемый объект
(список, строку, кортеж, словарь, множество) и вычисляет сумму только целых четных чисел, взятых из элементов
итерируемого объекта. Результат возвращается функцией. Если целых чисел нет, то возвращается 0.

Сигнатура функции должна быть, следующей:

def get_even_sum(it): ...

Вызывать функцию не нужно, только определить. Также ничего не нужно выводить на экран.

P. S. Не забудьте про необходимость различения булевых значений (False, True) от целочисленных.
"""

def get_even_sum(it):
    res = 0
    for x in it:
        if isinstance(x, int) and not isinstance(x, bool): # Проверка на целые числи и что тип данных не булево значение.
            if x % 2 == 0:
                res += x
        else:
            continue

    return res

if __name__ == "__main__":
    print(get_even_sum([1, 2, 3, "a", True, [4, 5], "c", (4, 5)]))
    print(get_even_sum({5, 6, 7, '8', 5, '4'}))
    print(get_even_sum((10, "f", '33', True, 12)))
    print(get_even_sum(['1', True, False, (1, 23)]))