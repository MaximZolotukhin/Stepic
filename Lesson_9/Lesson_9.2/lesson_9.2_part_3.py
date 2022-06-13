"""
9.2 Функция-генератор. Оператор yield

Подвиг 3. Вводится натуральное число N (N > 8). Необходимо определить функцию-генератор,
которая бы выдавала пароль длиной N символов из случайных букв, цифр и некоторых других знаков.
Для получения последовательности допустимых символов для генерации паролей в программе импортированы
две строки: ascii_lowercase, ascii_uppercase (см. листинг ниже), на основе которых формируется общий список:

from string import ascii_lowercase, ascii_uppercase
chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"

Функция-генератор должна при каждом вызове возвращать новый пароль из случайно выбранных символов chars длиной N
и делать это бесконечно, то есть, вызывать ее можно бесконечное число раз. Сгенерировать случайный индекс indx
в диапазоне [a; b] для символа можно с помощью функции randint модуля random:

import random
random.seed(1)
indx = random.randint(a, b)

Сгенерируйте с помощью этой функции первые пять паролей и выведите их в столбик (каждый с новой строки).

Sample Input: 10
Sample Output:
riGp?58WAm
!dX3a5IDnO
dcdbWB2d*C
4?DSDC6Lc1
mxLpQ@2@yM
"""

import random
from string import ascii_lowercase, ascii_uppercase

# установка зерна датчика случайных чисел (не менять)
random.seed(1)
N = int(input())

# здесь продолжайте программу

import random
def gen_passwords():
    chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"
    index = random.randint(0, 68)
    yield chars[index]



if __name__ == "__main__":
    count = 5
    while count > 0:
        num = N
        while num > 0:
            val_def = gen_passwords()
            print(*val_def, end='')
            num -= 1
        print()
        count -= 1


#
# import random
# def gen_passwords(N):
#     chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"
#     passwords = ''
#     while N > 0:
#         index = random.randint(0, 68)
#         passwords += chars[index]
#         N -= 1
#     yield passwords
#
#
# if __name__ == "__main__":
#     count = 5
#     while count > 0:
#         val_def = gen_passwords(N)
#         print(*val_def)
#         count -= 1
