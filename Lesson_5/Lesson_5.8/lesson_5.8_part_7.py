"""
5.8 Генераторы списков (List comprehension)

Подвиг 7. Вводится список вещественных чисел. С помощью list comprehension сформировать список,
состоящий из элементов введенного списка, имеющих четные индексы (то есть, выбрать все элементы
с четными индексами). Результат вывести на экран в одну строку через пробел.

Sample Input: 8.5 11.3 1.0 -4.5 11.34 6.45
Sample Output: 8.5 1.0 11.34
"""

num_list = input().split() # Пользовательский ввод

num_index = [num_list[num] for num in range(0, len(num_list)) if float(num) % 2 == 0] # Выбираю элементы по индексу
# если он идут под четными индексами в списке
print(*num_index)

# Решение второй вариант
num_index_2 = [value for num, value in enumerate(num_list) if float(num) % 2 == 0]
print(*num_index_2)