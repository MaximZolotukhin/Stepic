"""
5.2 Операторы break, continue и else

Подвиг 9. (На использование цикла while). Вводятся названия книг (каждое с новой строки).
Удалить из введенного списка все названия, состоящие из двух и более слов (слова в названиях разделяются пробелом).
Результат вывести на экран в виде строки из оставшихся названий через пробел.

P. S. Для считывания списка целиком в программе уже записаны начальные строчки

Sample Input:
Муму
Евгений Онегин
Сияние
Мастер и Маргарита
Пиковая дама
Колобок

Sample Output: Муму Сияние Колобок
"""

import sys #Подключаю библиотеку sys


# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

index = 0 # Переменная для расчета индекса
while index < len(lst_in): # Пока индекс меньше длинны списка
    if ' ' in lst_in[index]: # Если находим пробел в списке
        lst_in.pop(index) # Удаляем его
        index -= 1 # Сдвигаем индекс на 1 шаг назад так как длинна списка уменьшилась и мы можем пропустить символ
    else: # Иначе
        index += 1 # Увеличиваем индекс на 1

print(*lst_in) # Выводим результат
