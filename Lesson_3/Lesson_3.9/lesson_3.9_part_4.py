"""
3.9 Вложенные списки

Подвиг 6. Имеется вложенный список из трех строк:
t = [["Скажи-ка", "дядя", "ведь", "не", "даром"],
    ["Я", "Python", "выучил", "с", "каналом"],
    ["Балакирев", "что", "раздавал?"]]
Необходимо реализовать проверку на наличие в этом списке введенного слова.
Результат (True или False) вывести на экран. Решить задачу необходимо без применения условного оператора.

Sample Input: дядя
Sample Output: True
"""

# Сохраняю стихотворение
verse = [["Скажи-ка", "дядя", "ведь", "не", "даром"],
    ["Я", "Python", "выучил", "с", "каналом"],
    ["Балакирев", "что", "раздавал?"]]
# Сохраняю проверочное слово
word = input()
# Проверяю его наличие в вложенных списках, через оператор in
value = word in verse[0] or word in verse[1] or word in verse[2]
# Вывожу в консоль полученный результат
print(value)
