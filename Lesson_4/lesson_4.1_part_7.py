"""
4.1 Условный оператор if. Конструкция if-else

Подвиг 7. Вводится список городов в одну строку через пробел. Если в этом списке присутствует город Москва,
то удалить его. Вывести на экран результирующий список в виде строки с городами через пробел.

Sample Input: Уфа Астрахань Москва Самара Казань
Sample Output: Уфа Астрахань Самара Казань
"""
# Присваиваю данные в переменную
list_word = list(input().split())
# Если в этом списке присутствует город Москва
if 'Москва' in list_word:
    list_word.remove('Москва') # то удаляю его с помощью метода .remove('Москва')
    print(*list_word) # Вывожу результат в консоль
else:
    print(*list_word) # Вывожу результат в консоль
