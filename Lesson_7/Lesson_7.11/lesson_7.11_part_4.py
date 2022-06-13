"""
7.11 Декораторы функций

Подвиг 4. Вводятся две строки из слов (слова записаны через пробел). Объявите функцию,
которая преобразовывает эти две строки в два списка слов и возвращает эти списки.
Определите декоратор для этой функции, который из двух списков формирует словарь,
в котором ключами являются слова из первого списка, а значениями - соответствующие элементы из второго списка.
Полученный словарь должен возвращаться при вызове декоратора.
Примените декоратор к первой функции и вызовите ее для введенных строк.
Результат (словарь d) отобразите на экране командой:
print(*sorted(d.items()))

Sample Input:
house river tree car
дом река дерево машина

Sample Output:
('car', 'машина') ('house', 'дом') ('river', 'река') ('tree', 'дерево')
"""

word_1 = input()
word_2 = input()

def create_dict(any_fanc): # Внешняя функция-декоратор
    def wrapper(*args): # Внутренняя функция
        list_in = any_fanc(*args) # Функция которая будет обработана
        list_work = list_in[0] # Вывожу первый вложенный список в отдельное список
        res_dict = {} # Созадаю пустой словарь
        for index, val in enumerate(list_in[1]): # Перебираю значения из вложенного списка №2, с помощью enumerate
            # для упрощения задачи извлечения значений из списков. Таким образом из второго вложенного списка я получаю
            # значения и сохраняю его как значение, а из первого вложенного списка я получаю значения по индексу,
            # индекс меняется с помощью enumerate, эти значения я использую для ключей в словаре
            res_dict[list_work[index]] = val

        return res_dict
    return wrapper

@create_dict
def string_to_list(*args):
    list_val = [] # Пустой список
    for val_str in args: # Вытаскиваю значения из полученного кортежа
        res = [val for val in val_str.split()] # Разбиваю полученную строку на элементы и сохраняю в список через генератор списков
        list_val.append(res) # Добавлюя полученное значение в кортеж
    return list_val # Возвращаю полученный список


print(*sorted(string_to_list(word_1, word_2).items()))

# -----------------   Виртуозный варинат решения -------------------------
def get_2dict(func):
    def wrapper(*args, **kwargs):
        return dict(zip(*func(*args, **kwargs)))
    return wrapper

@get_2dict
def get_2list(word1, word2):
    return [word1.split(), word2.split()]


d = get_2list(input(), input())
print(*sorted(d.items()))


# -----------------   Более грамотный чем мой  -------------------------

def lst_dic(func):
    def dic_trans(*args):
        keys, values = func(str1, str2)
        d = {keys[i]: values[i] for i in range(len(keys))}
        return d

    return dic_trans


str1, str2 = input(), input()


@lst_dic
def str_lst(str1, str2):
    lst1 = list(str1.split())
    lst2 = list(str2.split())

    return lst1, lst2


d = str_lst(str1, str2)
print(*sorted(d.items()))