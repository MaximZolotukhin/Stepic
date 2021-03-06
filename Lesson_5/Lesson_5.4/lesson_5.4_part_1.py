"""
5.4 Примеры работы оператора цикла for. Функция enumerate

Подвиг 1. Вводится строка. Необходимо найти все индексы фрагмента "ра" во введенной строке. Вывести в строку через пробелы найденные индексы. Если этот фрагмент ни разу не будет найден, то вывести значение -1.

Sample Input: Барабанщик бил бой в барабан
Sample Output: 2 23
"""

text = input().lower() # Получаю строку и перевожу все символы в нижний регистр
res_count = 0 # Сюда буду записывать индексы

if 'ра' in text: # Проверяю есть ли вообще в переданном тексте сочетание букв 'ра', если нет то работа программы не имеет смысла
    for i in range(0, text.count('ра')): # Перебираю текст циклом для нахождения всех индексов, text.count('ра')
        # - вернет сколько раз встречается 'ра' в тексте, чтобы цикл не делал лишней итерации
        if 'ра' in text:  # Проверяю есть ли в переданном тексте сочетание букв 'ра', для вывода индекса
            res_count = text.find('ра', res_count if i == 0 else res_count + 1) # Если нахожу сохраняю в переменную, res_count + 1 использую
            # для дальнейшего прохода, иначе будет находить все время одни и тот же индекс.
            print(res_count, end=' ') # Вывожу результат
else:
    print('-1') # проверка не пройдена возвращаю -1

