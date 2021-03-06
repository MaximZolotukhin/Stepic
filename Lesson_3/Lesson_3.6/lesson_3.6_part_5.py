"""
3.6 Списки и операции над ними

Подвиг 8. Вводится информация по книге (каждое значение с новой строки):
название, автор, число страниц (целое число), цена (вещественное число).
На основе этих данных формируется список book с элементами в порядке их ввода.
Затем, из этого списка необходимо удалить 3-й элемент (число страниц),
в качестве автора записать "Пушкин" и цену увеличить в 2 раза.
Результат вывести на экран командой:

print(book)

Sample Input:
Мастер и Маргарита
Булгаков
233
435.45

Sample Output: ['Мастер и Маргарита', 'Пушкин', 870.9]
"""

# Сохраняем данные в перемененные
name_book = input()
name_author = input()
pages = int(input())
price = float(input())

# Создаем список(list) и вносим туда сохраненные данные
book = [name_book, name_author, pages, price]
# Удаляем данные из списка по индексу с помощью оператора del (удаляется число страниц - 233)
del book[2]
# Заменяем значение по первому индексу (заменяем Булгакова на Пушкина)
book[1] = 'Пушкин'
# Увеличиваем цену в два раза
book[2] *= 2
# Выводим результат
print(book)
