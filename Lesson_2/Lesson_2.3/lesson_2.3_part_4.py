"""
2.3 Математические функции и модуль math

Подвиг 5. Допишите текст программы для вычисления евклидового расстояния (гипотенузы) по перемещениям a и b (формула: ).
Округлите результат с точностью до сотых. Полученное значение выведите на экран.

Sample Input: 3 4
Sample Output: 5.0
"""

# функция map() - принимает функцию и аргумент составного типа данных, в нашем случае мы получаем введенные символы
# и преобразуем их в тип integer
# метод split() - разбивает строку по указанному разделителю, разделитель можно не указывать
a, b = map(int, input().split())

## функция round(число, количестов знаков после запятой) - округлять число с плавающей точкой до
# указанного количества знаков после запятной, второй аргумент не обязательный.
# функция pow(x, y) - используется для получения значения x в степени y
# math.sqrt(значения из которого извлекают корень) или a ** 0.5 используются для извлечения квадратного корня из значения
print(round((pow(a, 2) + pow(b, 2)) ** 0.5, 2))
