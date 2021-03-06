"""
5.3 Оператор цикла for и функция range

Подвиг 5. Вводятся целые числа в одну строчку через пробел. Необходимо преобразовать
эти данные в список целых чисел. Затем, перебрать этот список в цикле for и просуммировать
все нечетные значения. Результат вывести на экран.

Sample Input: 8 11 -2 4 0 13 19 12 7
Sample Output: 50
"""

# Пользовательский ввод
list_num = list(map(int, input().split()))
result = 0 # Переменная для сохранения результата
for i in list_num: # Перебираю значения в списке
    if i % 2 != 0: # Если остаток от деления не равен 0 значит число нечетное
        result += i # Суммирую значения

print(result)
