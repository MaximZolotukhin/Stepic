"""
3.5 Форматирование строк и F-строки

Подвиг 2. Вводятся: габариты изделия (целые числа): ширина, глубина, высота -
в одну строчку через пробел. С помощью метода format, используя ключи в качестве имен переменных,
сформировать строку: "Габариты: <ширина> x <глубина> x <высота>". Результат вывести на экран.

Sample Input: 8 11 13
Sample Output: Габариты: 8 x 11 x 13
"""

# Производим множественное сохранение в переменные с помощью функции map, input, разделяя их по пробелу с помощью split
wight, height, size = map(str, input().split())
# Выводим данные с помощью метода .format(x=wight, y=height, z=size),
# так же мы присваиваем конкретное значение каждой переменной в format
print("Габариты: {x} x {y} x {z}".format(x=wight, y=height, z=size))