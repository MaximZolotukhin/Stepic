"""
10.2 Битовые операции И, ИЛИ, НЕ, XOR

Подвиг 6. На вход программы подается целое десятичное число. Используя битовые операции,
выполните целочисленное деление введенного числа на 2. Результат отобразите на экране.

Sample Input:
22

Sample Output:
11
"""

# Побитовый свдиг влево умонжает число на кратное двум x<<n
x = int(input())
x = x>>1  # Обнуление 4 бита

print(x)
