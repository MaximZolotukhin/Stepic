"""
3.2 Индексы и срезы строк

Подвиг 7. Вводятся две строки (каждая с новой строчки). Из первой строки выделить
все символы с четными индексами, а из второй - с нечетными. Объединить строки
через пробел и вывести на экран.

Sample Input:
Hello
Python
Sample Output: Hlo yhn
"""
# Сохранения данных в переменную
st_1 = input()
st_2 = input()
# выводим все символы начиная со 2 и через одни символ
print(st_1[0::2] + " " + st_2[1::2])
