"""
10.3 Модуль random стандартной библиотеки

Значимый подвиг 7. Имеется двумерное игровое поле размером N x N (N - натуральное число, вводится с клавиатуры),
представленное в виде вложенного списка:

P = [[0] * N for i in range(N)]
Требуется расставить в нем случайным образом M = 10 единиц (целочисленных) так,
чтобы они не соприкасались друг с другом (то есть, вокруг каждой единицы должны быть нули, либо граница поля).

P.S. Поле на экран выводить не нужно (вообще ничего не нужно выводить), только сформировать.

Sample Input:
10

Sample Output:
True
"""
import random
# установка "зерна" датчика случайных чисел, чтобы получались одни и те же случайные величины
random.seed(1)
# начальная инициализация поля (переменные P и N не менять, единицы записывать в список P)
N = int(input())
P = [[0] * (N + 2) for i in range(N + 2)] # Формируем матрицу с дополнительными нулями по периметру

x = 10 # Счетчки 1 которые нам нужно разместить
while x > 0:# Начинаем заполнять цикл
    row = random.randint(1, N) # случайные координаы по строкам
    col = random.randint(1, N) # случайные координаы по столбцам
    # Проверка если вокруг полученных координат нет 1 то мы ее туда размещаем
    if P[row][col] + P[row + 1][col] + P[row - 1][col] + P[row][col + 1] + P[row][col - 1] + P[row + 1][col + 1] + P[row + 1][col - 1] + P[row - 1][col + 1] + P[row - 1][col - 1] == 0:
        P[row][col] = 1
        x -=1 # И удаляем одну единицу из необходимых

    else:
        continue

P = list(i[1:-1] for i in P[1:-1]) # Удаляем дополнительные нули)
# Отрисовываем результат
for i in P:
    print(*i)
