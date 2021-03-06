"""
6.6 Генераторы множеств и словарей

Подвиг 6. Вводится список книг книжного магазина в формате:
<автор 1>:<название 1>
...
<автор N>:<название N>

Авторы с названиями могут повторяться. Необходимо, используя генераторы, сформировать словарь с именем d вида:
{'автор 1': {'название 1', 'название 2', ..., 'название M'}, ..., 'автор K': {'название 1', 'название 2', ..., 'название S'}}
То есть, ключами выступают уникальные авторы, а значениями - множества с уникальными названиями книг соответствующего автора.
На экран ничего выводить не нужно, только сформировать словарь обязательно с именем d - он, далее будет проверяться в тестах!
P. S. Для считывания списка целиком в программе уже записаны начальные строчки.

Sample Input:
Пушкин: Сказака о рыбаке и рыбке
Есенин: Письмо к женщине
Тургенев: Муму
Пушкин: Евгений Онегин
Есенин: Русь

Sample Output:
True
"""
import sys
# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))
list_in_two = [val.split(': ') for val in lst_in]# Разделяю по ': ' получаю двумерный список
# здесь продолжайте программу (используйте список lst_in)'
d = dict()  # Создаю пустой словарь
for key, val in list_in_two: # Создаю пустой словарь
    if  d.get(key, False): # Если ключа нет возвращаю False и перехожу к опции else
        d[key].add(val) # Если ключ есть я захожу в условный оператор и добавляю значение к ключу
    else:
        d[key] = {val,}

print(d.items())
