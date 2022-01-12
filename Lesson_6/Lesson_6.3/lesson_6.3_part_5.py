"""
6.3 Кортежи (tuple) и их методы

Подвиг 5. Вводятся названия городов в одну строку через пробел. На их основе формируется кортеж.
Если в этом кортеже присутствует город "Ульяновск", то этот элемент следует удалить (создав новый кортеж).
Результат вывести на экран в виде строки с названиями городов через пробел.

Sample Input: Воронеж Самара Тольятти Ульяновск Пермь
Sample Output: Воронеж Самара Тольятти Пермь
"""

values_users = tuple(input().split()) # Создаем кортеж из пользовательских данных,
# разбивая на отдельные слова по пробелу с помощью метода .split()
# Так как КОРЕЖ неизменяемый тип данных мы можем только объединить кортежи или создать новый
# if 'Ульяновск' in values_users:
tup_city = tuple([i for i in values_users if i != 'Ульяновск']) #Создаю новый кортеж в него с помощью генератора списка
# перебираю значения из пользовательского кортежа и если значение не равно 'Ульяновск' сохраняю в новый кортеж

print(*tup_city)
