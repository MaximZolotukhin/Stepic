"""
6.3 Кортежи (tuple) и их методы

Подвиг 3. Имеется кортеж:
t = (3.4, -56.7)

Вводится последовательность целых чисел в одну строчку через пробел.
Необходимо их добавить в кортеж t. Результат вывести на экран командой:
print(t)

Sample Input: 8 11 -5 2
Sample Output: (3.4, -56.7, 8, 11, -5, 2)
"""

t = (3.4, -56.7) # Создаем кортеж
values_users = tuple(map(int, input().split())) # Создаем кортеж из пользовательских данных, преобразовываем их в int
# и разбивая на отдельные числа по пробелу с помощью метода .split()
# Так как КОРЕЖ неизменяемый тип данных мы можем только объединить кортежи или создать новый
t = t + values_users # Добавляем наш кортеж к начальному кортежу
print(t)
