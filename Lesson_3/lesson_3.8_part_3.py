"""
3.8 Методы списков

Подвиг 4. Вводится строка с номером телефона в формате:
+7(xxx)xxx-xx-xx
Необходимо преобразовать ее в список lst (посимвольно, то есть, элементами списка будут
являться отдельные символы строки). Затем, удалить первый '+', число 7 заменить на 8 и убрать дефисы.
Отобразить полученный список на экране командой:
print("".join(lst))

Sample Input: +7(912)123-45-67
Sample Output: 8(912)1234567
"""

# Сохраняем данные в переменную
strin = input()
# Преобразуем в список
lst = list(strin)
# Удаляем два первых элемента
lst.pop(0)
lst.pop(0)
# С помощью метода remove("-") удаляем тире
lst.remove("-")
lst.remove("-")
# С помощью метода insert(0,'8') вставляем на первое место число 8
lst.insert(0,'8')
# Метод join отвечает за объединение списка строк с помощью определенного указателя
print("".join(lst))
