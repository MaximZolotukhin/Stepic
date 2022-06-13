"""
9.2 Функция-генератор. Оператор yield

Подвиг 4. Вводится натуральное число N. Используя строки из латинских букв ascii_lowercase и ascii_uppercase:

from string import ascii_lowercase, ascii_uppercase
chars = ascii_lowercase + ascii_uppercase

задайте функцию-генератор, которая бы возвращала случайно сформированные email-адреса с доменом mail.ru и
длиной в N символов. Например, при N=6, получим адрес: SCrUZo@mail.ru
Для формирования случайного индекса для строки chars используйте функцию randint модуля random:

import random
random.seed(1)
index = random.randint(0, len(chars)-1)

Функция-генератор должна возвращать бесконечное число таких адресов, то есть, генерировать постоянно.
Выведите первые пять сгенерированных email и выведите их в столбик (каждый с новой строки).

Sample Input: 8
Sample Output:
iKZWeqhF@mail.ru
WCEPyYng@mail.ru
FbyBMWXa@mail.ru
SCrUZoLg@mail.ru
ubbbPIay@mail.ru
"""
from string import ascii_lowercase, ascii_uppercase
import random
random.seed(1)

N = int(input())


def gen_mails():
    chars = ascii_lowercase + ascii_uppercase
    index = random.randint(0, len(chars)-1)
    yield chars[index]


if __name__ == "__main__":
    count = 5
    while count > 0:
        num = N
        while num > 0:
            val_def = gen_mails()
            print(*val_def, end='')
            num -= 1
        print('@mail.ru')
        count -= 1

