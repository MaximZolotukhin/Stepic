"""
10.2 Битовые операции И, ИЛИ, НЕ, XOR

Подвиг 3. На вход программы подается целое десятичное число. Используя битовые операции,
выключите 4-й и 1-й биты введенного числа. Выведите на экран полученное числовое значение.

P. S. Распределение номеров бит представлено на следующем рисунке.

Sample Input:
153

Sample Output:
137
"""
# Обнуление n-ого бита x &= ~(1<<1)
x = int(input())
x &= ~(1<<1)   # Обнуление 1 бита
x &= ~(1<<4)   # Обнуление 4 бита

print(x)

#Вариант 2
print(int(input()) & ~(1 << 1) & ~(1 << 4))