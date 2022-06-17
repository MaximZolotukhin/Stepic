"""
9.8 Функция isinstance для проверки типов данных

Подвиг 5. Определите функцию с именем get_list_dig, которая возвращает список
только из числовых значений переданной ей коллекции (список или кортеж).

Сигнатура функции должна быть, следующей:
def get_list_dig(lst): ...

Вызывать функцию не нужно, только определить. Также ничего не нужно выводить на экран.
P. S. Не забудьте про необходимость различения булевых значений (False, True) от целочисленных.
"""
lst = [1, 2, 3, "a", True, [4, 5], "c", (4, 5), 4.8, 12.6]

def get_list_dig(lst):
    result = list()
    for x in lst:
        if isinstance(x, (int, float)) and not isinstance(x, (bool)):
            result.append(x)

    return result

if __name__ == "__main__":
    print( get_list_dig(lst))