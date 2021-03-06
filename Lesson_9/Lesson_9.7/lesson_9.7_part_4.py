"""
9.7 Аргумент key для сортировки по ключу

Подвиг 3. Известно, что порядок нот, следующий: до, ре, ми, фа, соль, ля, си. На вход программы
поступает строка с набором этих нот, записанных через пробел. Необходимо сформировать список из
входной строки с нотами, отсортированными указанным образом. Результат вывести в виде строки из нот,
записанными через пробел.

Sample Input: до фа соль до ре фа ля си

Sample Output: до до ре фа фа соль ля си
"""

note = list(input().split()) # Создаем список
note_2 = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си'] # Тестовый список

b = sorted(note, key=lambda x: note_2.index(x)) # Сортируем список по совпадения с индексом тестового списка
print(*b)

