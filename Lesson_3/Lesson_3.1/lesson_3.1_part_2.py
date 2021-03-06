"""
3.1 Введение в строки. Операции над строками

Подвиг 7. Напишите программу ввода двух слов через пробел. Сформируйте новую строку,
продублировав первое слово дважды, а второе - трижды (все слова в результирующей
строке должны идти через пробел). Результат выведите на экран.
Программу следует реализовать без использования F-строк, а с применением оператора дублирования строк.

Sample Input: hello python
Sample Output: hello hello python python python
"""

# Производим множественное сохранение в переменные с помощью функции map, input, разделяя их по пробелу с помощью split
str_1, str_2 = map(str, input().split())

print((str_1 + " ") * 2 + (str_2 + " ") * 3) # Выводим строки увеличивая их число в 2 и 3 раза.
