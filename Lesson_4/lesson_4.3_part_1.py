"""
4.3 Тернарный условный оператор

Подвиг 1. Вводится два вещественных числа, каждое с новой строки.
Необходимо с помощью тернарного условного оператора наибольшее значение
присвоить переменной d и вывести ее на экран.

Sample Input:
5.4
-3.8
Sample Output:
5.4
"""

# Сохраняю данные в переменные
a = float(input())
b = float(input())

# Работа тернарного оператора:
'''
Если а больше b, тогда данные сохраняем в a, иначе сохраняем в b.
Далее полученные результат сохраняем в переменную result
'''
result = a if a > b else b
print(result)
