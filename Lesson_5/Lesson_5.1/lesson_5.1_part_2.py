"""
5.1 Оператор цикла while

Подвиг 3. Вводится стоимость одной книги x рублей (вещественное число).
Необходимо вывести на экран в строчку через пробел стоимости 2, 3, ...
10 таких книг с точностью до десятых. Программу реализовать при помощи цикла while.

Sample Input: 34.6
Sample Output: 69.2 103.8 138.4 173.0 207.6 242.2 276.8 311.4 346.0
"""

# Присваиваем значение в переменную
n = float(input())
i = 2 # счетчик так как минимальная стоимость 2 начинаем с этого знанчения
while i < 11:
    print(round(n * i, 1), end=' ') # Вывожу в консоль.
    i += 1 # Увеличиваю i на один при каждой итерации цикла.