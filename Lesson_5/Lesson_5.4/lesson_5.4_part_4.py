"""
5.4 Примеры работы оператора цикла for. Функция enumerate

Подвиг 4. Вводится список в виде целых чисел в одну строку через пробел.
Необходимо сначала сформировать список на основе введенной строки, а затем,
каждое значение этого списка изменить, возведя в квадрат. Отобразить результат
на экране в виде строки полученных чисел, записанных через пробел.
Программу следует реализовать с использованием функции enumerate.

Sample Input: 8 -11 4 3 6
Sample Output: 64 121 16 9 36
"""
# Сохраняем в список
numbers_list = list(map(int, input().split()))
# enumerate возвращает индек и значение
for index, value in enumerate(numbers_list): # Сохраняем в список  и перебираем его с помощью enumerate
    numbers_list[index] = value ** 2 # Возводим в степерь

print(*numbers_list)
