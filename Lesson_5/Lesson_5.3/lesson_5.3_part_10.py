"""
5.3 Оператор цикла for и функция range

Подвиг 10. Вводится натуральное число n. Вычислить сумму всех натуральных чисел меньше n,
которые кратны или 3 или 5. Результат (сумму) вывести на экран. Пример: n = 10,
имеем числа: 3, 5, 6, 9. Их сумма равна 23.

Sample Input: 21
Sample Output: 98
"""

number = int(input()) # Пользовательский ввод
result = 0  # Переменная для хранения результата

for i in range(1, number): # Перебираем все значения от 1 до заданного пользователем
    if i % 5 == 0 or i % 3 == 0: # Если остаток от деления на 5 и 3 равен 0 тогда прибавляем его с result
        result += i  # прибавляем его с result

print(result) # Выводим результат
