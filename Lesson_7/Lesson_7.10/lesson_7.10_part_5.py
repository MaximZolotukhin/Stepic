"""
7.10 Замыкания в Python. Вложенные функции

Подвиг 5. Используя замыкания функций, объявите внутреннюю функцию, которая преобразует строку из списка целых чисел,
записанных через пробел, либо в список, либо в кортеж. Тип коллекции определяется параметром tp внешней функции.
Если tp = 'list', то используется список, иначе (при другом значении) - кортеж.

Далее, на вход программы поступают две строки: первая - это значение для параметра tp;
вторая - список целых чисел, записанных через пробел. С помощью реализованного замыкания преобразовать эти
данные в соответствующую коллекцию. Результат вывести на экран командой (lst - ссылка на коллекцию):

print(lst)

Sample Input:
list
-5 6 8 11 0 111 -456 3

Sample Output:
[-5, 6, 8, 11, 0, 111, -456, 3]
"""
tp = input()
string = input()

def string_in_number(tp='list'):
    def converter(string):
        if tp == 'list':
            result = [int(num) for num in string.split()]
            return result
        elif  tp == 'tuple':
            result = tuple(int(num) for num in string.split())
            return result
    return converter


zamok = string_in_number(tp)
# print(type(zamok(string)))
print(zamok(string))
