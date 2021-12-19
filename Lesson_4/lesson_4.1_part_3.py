"""
4.1 Условный оператор if. Конструкция if-else

Подвиг 3. Вводятся два целых положительных числа m и n в одну строку через пробел.
Если число m делится нацело на число n, то вывести на экран частное от деления (результат деления)
в виде целого числа. В противном случае вывести сообщение «m на n нацело не делится» (без кавычек)
и вместо m и n подставить соответствующие числа, например: «13 на 2 нацело не делится».

Sample Input 1: 8 4
Sample Output 1: 2
Sample Input 2: 11 2
Sample Output 2: 11 на 2 нацело не делится
"""
# Множественное присваивание
m, n = map(int, input().split())
# Проверяем делится ли число на цело
if m % n == 0:
    print(int(m/n)) # Выводим в консоль частное от деления
else:
    print(f"{m} на {n} нацело не делится") # Иначе.
