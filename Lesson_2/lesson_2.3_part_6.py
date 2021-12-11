"""
2.3 Математические функции и модуль math

Подвиг 7. В летний лагерь нужно отвести n детей и m вожатых с помощью автобусов.
Максимальная вместимость каждого автобуса 20 человек. Допишите программу для вычисления
минимального числа автобусов, необходимых для перевозки детей вместе с вожатыми.
Результат выведите в консоль в виде целого числа.

Sample Input: 40 5
Sample Output: 3
"""

import math # Подключаю библиотеку math

# ввод данных
n, m = map(int, input().split())

# ceil - округление до ближайшего большего числа
print(math.ceil((n + m) / 20))