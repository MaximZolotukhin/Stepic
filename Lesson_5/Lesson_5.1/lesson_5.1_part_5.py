"""
5.1 Оператор цикла while

Подвиг 6. Вводится строка (слаг). Замените в этой строке все подряд идущие
дефисы (--, ---, ---- и т.д.) на одинарные (-). Результат преобразования строки
выведите на экран. Программу реализовать при помощи цикла while.

Sample Input:
osnovnye--metody-----slovarey

Sample Output:
osnovnye-metody-slovarey
"""

# Сохраняю данные в переменную
begin_string = input()
count = len(begin_string) # Делаю счетчик длинной в веденной слово
simbol = '--'   # Делаю шаблон символов которые нужно будет удалить.
while count != 0: # Пока счетчик не равен 0
    begin_string = begin_string.replace(simbol,'-') # Заменяю все -- на -
    count -= 1  # уменьшает счетчик

print(begin_string) # Выводим результат
