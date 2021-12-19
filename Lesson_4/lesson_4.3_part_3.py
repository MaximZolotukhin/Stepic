"""
4.3 Тернарный условный оператор

Подвиг 3. Вводится слово. Переменной msg присвоить строку "палиндром",
если введенное слово является палиндромом (одинаково читается и вперед и назад),
а иначе присвоить строку "не палиндром". Проверку проводить без учета регистра.
Программу реализовать с помощью тернарного условного оператора.
Значение переменной msg отобразить на экране.

Sample Input: Казак
Sample Output: палиндром
"""

# Сохраняю слово в переменную и сразу перевожу буквы в нижний регистр с помощью метода .lower()
msg = input().lower()
# Копирую слово в обратном порядке
msg_2 = msg[::-1]
# Копирую слово в обратном порядке и проверяю его с помощью тернарного оператора
result = "палиндром" if msg == msg_2 else "не палиндром"
print(result)