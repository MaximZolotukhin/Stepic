"""
6.4 Множества (set) и их методы

Подвиг 8. Пользователь с клавиатуры вводит названия городов, пока не введет букву q.
Определить общее уникальное число городов, которые вводил пользователь.
На экран вывести это число. Из коллекций при реализации программы использовать только множества.

Sample Input:
Уфа
Москва
Тверь
Екатеринбург
Томск
Уфа
Москва
q

Sample Output: 5
"""
set_1 = set() # Создаю пустое множество
while True: # Циклом запрашиваю данные у пользователя до того как он введет "q"
    symbol = input() # Запрашиваем данные у пользователя
    if symbol != 'q': # Если не введен 'q'
        set_1.add(symbol) # Добавляю данные к множеству с помощью метода add()
    else:
        break # Выхожу из цикла

print(len(set_1))

