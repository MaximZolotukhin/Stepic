"""
3.2 Индексы и срезы строк

Подвиг 8. Из введенной строки отобразить первые пять символов в обратном порядке.
Полагается, что введенная строка имеет минимум пять символов.

Sample Input: abrakadabra
Sample Output: karba
"""

st = input() # Сохраняю данные в переменную
st_1 = st[0:5] # сохраняю в перменную копию полученнго знанчения с нулеговго индекса до 4 включительно
print(st_1[::-1]) # Переворачиваю полученный результат с помощью среза.