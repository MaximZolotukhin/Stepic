"""
7.8 Анонимные (lambda) функции

Подвиг 4. Объявите анонимную (лямбда) функцию для вычисления модуля числа
(то есть, отрицательные числа нужно делать положительными).
Вызовите эту функцию для введенного числа x:

x = float(input())

Отобразите результат работы функции на экране.

Sample Input: -5.6
Sample Output: 5.6
"""
x = float(input())

mod = lambda x: ((x**2)**0.5) # Способ перевода из отрицательно в положительное число
mod_2 = lambda x: (abs(x)) # Способ перевода из отрицательно в положительное число

print(mod(x))
print(mod_2(x))