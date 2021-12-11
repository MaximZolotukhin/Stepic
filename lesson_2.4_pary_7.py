"""
Подвиг 9. В магазине продается X синих ручек, Y зеленых, черных в два раза больше, чем синих,
а красных в четыре раза больше зеленых. Напишите программу, в которой вводятся целые значения X, Y
в одну строку через пробел с помощью команды:

X, Y = map(int, input().split())

и выводится на экран общее число ручек в виде целого числа.

Sample Input: 10 20
Sample Output: 130
"""

# функция map() - принимает функцию и аргумент составного типа данных, в нашем случае мы получаем введенные символы
# переводя в тип integer
blue, green = map(int, input().split()) # Сохраняем количество синих и зеленых ручек


black = blue * 2 # Узнаем сколько черных ручек
red = green * 4 # Узнаем сколько красных ручек
sum = blue + green + black + red # Узнаем сколько ручек всех цветов всего
print(sum) # Выводим результат
