"""
5.1 Оператор цикла while

Подвиг 8. Последовательность Фибоначчи образуется так: первые два числа равны 1 и 1,
а каждое последующее равно сумме двух предыдущих. Имеем такую последовательность
 чисел: 1, 1, 2, 3, 5, 8, 13, ... Постройте последовательность Фибоначчи длиной n
 (n вводится с клавиатуры). Результат отобразите в виде строки полученных чисел,
 записанных через пробел. Программу реализовать при помощи цикла while.

Sample Input: 8
Sample Output: 1 1 2 3 5 8 13 21
"""

n = int(input()) # Пользовательский ввод
num_1 = 0 # Первое число
num_2 = 1 # Второе число
count = 1 # Счетчик
str_fib = '1' # Хранишище чисел Фибоначчи
fib = 1 # Одно из чисел Фибоначчи

while count < n:
    fib = num_1 + num_2 # Складывая первое число со вторым получаю следующее число фибоначи
    str_fib += f' {fib}' # Добавляю очередное число фибоначи в хранилище
    num_1 = num_2 # Первое число заменяю вторым
    num_2 = fib # Второе число заменяю полученным числом фибоначи
    count += 1 # Увеличиваю счетчки на 1

print(str_fib)
