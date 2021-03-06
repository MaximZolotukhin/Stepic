"""
7.7 Рекурсивные функции

Подвиг 3. Вводится список целых чисел в одну строчку через пробел.
Необходимо вычислить сумму этих введенных значений, используя рекурсивную функцию (для перебора элементов списка)
с именем get_rec_sum. Функция должна возвращать значение суммы. (Выводить на экран она ничего не должна).
Вызовите эту функцию и выведите вычисленное значение суммы на экран.

Sample Input: 8 11 -5 4 3
Sample Output: 21
"""

list_in = [int(num) for num in input().split()] # С помощью генератора списков создаю список входящих чисел


def get_rec_sum(list_in): # Функция которая возвращает значение списка и складывает его с удаленным значением
    if len(list_in) != 0: # Пока в списке есть хоть одно значение
        return list_in.pop() + get_rec_sum(list_in) # Удаляю значение из списка и вызываю функцию заново
    else:
        return 0 # Если итерации закончились тогда возвращаем 0


print(get_rec_sum(list_in))



# list_in = [int(num) for num in input().split()] # С помощью генератора списков создаю список входящих чисел
# result = 0 # Временная переменная для хранения результата, если помещаю в функцию она обнуляется
#
# def get_rec_sum(list_in, result):
#     result = result
#     if len(list_in) != 0:
#         result += list_in.pop()
#         return get_rec_sum(list_in, result)
#     else:
#         sum_all = result
#         return sum_all
#
#
# print(get_rec_sum(list_in, result))