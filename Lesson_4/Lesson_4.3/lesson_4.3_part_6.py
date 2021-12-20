"""
4.3 Тернарный условный оператор

Подвиг 6. Имеется список базовых нот:
m = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']
Вводятся три целых числа в диапазоне от 1 до 7 - номера нот,
в одну строчку через пробел. Необходимо отобразить указанные ноты
в виде строки через пробел, но перед нотами до и фа дополнительно
ставить символ диеза '#'. Реализовать эту программу с использованием
тернарного условного оператора.

Sample Input: 1 6 7
Sample Output: #до ля си
"""

# Создаю список с нотами
notes = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']
# Сохраняю переменные в список
number_note_1, number_note_2, number_note_3  = list(map(int, input().split()))
# Делаю список в котором буду хранить результат
new_list = []
# Если номер ноты не 1 или не 4: Выводи ноту без знака #, иначе выводим ноту с знаком #
new_list.append(f'#{notes[number_note_1-1]}' if number_note_1 == 1 or number_note_1 == 4 else f'{notes[number_note_1 - 1]}')
new_list.append(f'#{notes[number_note_2-1]}' if number_note_2 == 1 or number_note_2 == 4 else f'{notes[number_note_2 - 1]}')
new_list.append(f'#{notes[number_note_3-1]}' if number_note_3 == 1 or number_note_3 == 4 else f'{notes[number_note_3 - 1]}')
# Выводим результат
print(*new_list)
