"""
7.1 Что такое функции. Их объявление и вызов

Подвиг 3. Задайте функцию, которая не принимает никаких аргументов и просто выводит на экран строку:
It's my first function
В конце программы вызовите эту функцию.

Sample Input:

Sample Output: It's my first function
"""

def my_print(): # Создаем функцию без параметров
    text = 'It\'s my first function'
    print(text)


my_print() # Вызываем функцию
