"""
6.6 Генераторы множеств и словарей

Подвиг 2. Вводится строка со списком оценок, например:
2 неудовлетворительно удовлетворительно хорошо отлично
Первая цифра - это числовое значение первой оценки. Остальные оценки имеют возрастающие на 1 числа.
С помощью генератора словарей необходимо сформировать словарь d,
где ключами будут выступать числа, а значениями - слова.
Например:
d = {2: 'неудовлетворительно', 3: 'удовлетворительно', 4: 'хорошо', 5: 'отлично'}
Вывести на экран значение сформированного словаря с ключом 4.

Sample Input:
1 ужасно неудовлетворительно удовлетворительно прилично отлично

Sample Output:
прилично
"""

# считываю строчку, разделяю по пробелу
lst_in = [val for val in input().split()]
# проверяю с помощью метода .isalpha() пропускаем только буквы
list_if_alpha = [val for val in lst_in if val.isalpha()]

# За начало ключей беру int(lst_in[0]) значения из переданной строки
# 
number_auto = {key: val for key, val in enumerate(list_if_alpha, int(lst_in[0]))}
# Выводим элемент с индексом 4
print(number_auto[4])

