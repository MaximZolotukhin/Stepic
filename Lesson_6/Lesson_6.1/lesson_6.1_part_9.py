"""
6.1 Введение в словари

Подвиг 9. Пользователь вводит в цикле целые положительные числа, пока не введет число 0.
Для каждого числа вычисляется квадратный корень (с точностью до сотых) и значение выводится на экран (в столбик).
С помощью словаря выполните кэширование данных так, чтобы при повторном вводе того же самого числа
результат не вычислялся, а бралось ранее вычисленное значение из словаря. При этом на экране должно выводиться:

значение из кэша: <число>

Sample Input:
1
2
3
3
2
4
0

Sample Output:
1.0
1.41
1.73
Значение из кэша: 1.73
значение из кэша: 1.41
2.0
"""

cash = {} # Создаю словарь

while True: # Запускаю цикл для прохода по введенным пользователе цифрам
    num = int(input())  # Сбор пользовательское информации
    if num == 0: # Проверка на 0, если не сделать то будет выводить еще и ноль
        break # Тут прерываем работу программы.
    else:
        if num not in cash: # Выбираю из значения имя по индексу если ключа нет
            cash[num] = (round(num**0.5, 2))  # Добавляю в словарь ключи и значение, для значения вычисляю квадратный корень
            print(cash[num]) # Вывожу значение
        else: # Если ключ уже имеется тогда вывожу значение из словаря по ключу
            print(f"значение из кэша: {cash[num]}")


# while True: # Запускаю цикл для прохода по введенным пользователе цифрам
#     num = int(input())  # Сбор пользовательское информации
#     if num == 0:
#         break
#     else:
#         num_list.append(num)
#         print(num)
#
# for value in num_list:
#     if value not in cash: # Выбираю из значения имя по индексу если ключа нет
#         cash[value] = (round(value**0.5, 2))  # Добавляю в словарь ключи и значение, для значения вычисляю квадратный корень
#         print(round(value**0.5, 2)) # Вывожу значение
#     else: # Если ключ уже имеется тогда вывожу значение из словаря по ключу
#         print(f"Значение из кэша: {cash[value]}")