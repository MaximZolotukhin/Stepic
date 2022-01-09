"""
5.8 Генераторы списков (List comprehension)

Подвиг 5. Вводится натуральное число n. Необходимо сформировать список с помощью list comprehension,
состоящий из делителей числа n (включая и само число n). Результат вывести на экран в одну строку через пробел.

Sample Input: 10
Sample Output: 1 2 5 10
"""
user_number = int(input()) # Пользовательский ввод
list_number = [num for num in range(1, user_number+1) if user_number % num == 0] # Сохраняем значение в список если
# Остаток от его деления равен 0

print(*list_number)
