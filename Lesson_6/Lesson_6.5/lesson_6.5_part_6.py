"""
6.5 Операции над множествами. Сравнение множеств

Подвиг 6. Вводятся два списка городов каждый с новой строки (в строке названия через пробел),
которые объехал Сергей в 1-й и 2-й годы своего путешествия по России. Требуется определить,
включал ли его маршрут во 2-й год все города 1-го года путешествия? Если это так,
то вывести ДА, иначе - НЕТ.

Sample Input:
Москва Казань Самара Москва
Москва Владимир Новгород Казань Самара Москва

Sample Output: ДА
"""

set_1 = set(input().split()) # Получаем пользовательские данные
set_2 = set(input().split()) # Получаем пользовательские данные

print("НЕТ" if set_1 - set_2 else "ДА") # Когда мы из set_1 вычетаем set_2, то стираем все значения которые есть
# в set_2 из set_1. Если после этого в set_1 не остается ни одного элемента, то это значит что все города из второго
#множества удалены значнение пустое возвращает False
# значит мы выполняем условие задания, если хоть один город останится тогда мы не выполняем условия задачи и какойто
# город не был посещен значнение будет равно больше 0 Значнит True
# Второй варинат решения
print("НЕТ" if set_2.issubset(set_1) else "ДА")