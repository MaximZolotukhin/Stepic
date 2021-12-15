"""
3.6 Списки и операции над ними

Подвиг 7. Вводятся оценки студента (целые числа от 2 до 5) в одну строчку через пробел. На основе введенной строки формируется список командой:

marks = list(map(int, input().split()))

Необходимо вычислить средний балл и вывести его на экран с точностью до десятых (один знак после запятой).

Sample Input: 3 3 2 4 4 5 4 3 2
Sample Output: 3.3
"""

# Сохраняем данные в перемененную
marks = list(map(int, input().split()))
# C помощью функции sum мы получаем сумму всех чисел в списке
# C помощью функции len мы считаем сколько чисел в списке (получаем длину списка)
# Потом делим длину списка на сумму всех числе (получаем среднее значение)
result = sum(marks) / len(marks)
# Выводим результат и округляем его до 1 знака после запятой
print(round(result, 1))