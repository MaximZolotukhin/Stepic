"""
4.1 Условный оператор if. Конструкция if-else

Подвиг 5. Вводится четырехзначное число. Проверить, что оно оканчивается на цифру 7.
Вывести на экран ДА, если это так и НЕТ - в противном случае.

Sample Input: 8117
Sample Output: ДА
"""
# Присваиваю данные в переменную
list_num = list(input())
# Проверить, что оно оканчивается на цифру 7
if int(list_num[-1]) == 7: # Преобразую из строкового значения в int обращаюсь к последнему элементу и сравниваю
    print("ДА") # Если условие выполняется выводим ДА
else:
    print("НЕТ") # Иначе выводим НЕТ
