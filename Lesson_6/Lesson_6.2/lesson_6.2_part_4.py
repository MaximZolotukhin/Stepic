"""
6.2 Методы словаря. Перебор его элементов в цикле

Подвиг 4. Имеется закодированная строка с помощью азбуки Морзе. Коды разделены между собой пробелом.
Необходимо ее раскодировать, используя азбуку Морзе из предыдущего занятия.
Полученное сообщение (строку) вывести на экран.

Sample Input: .-- ... . -...- .-- . .-. -. ---
Sample Output: все верно
"""
morze = {'а': '.-', 'б': '-...', 'в': '.--', 'г': '--.', 'д': '-..', 'е': '.', 'ё': '.', 'ж': '...-',
         'з': '--..', 'и': '..', 'й': '.---', 'к': '-.-', 'л': '.-..', 'м': '--', 'н': '-.', 'о': '---',
         'п': '.--.', 'р': '.-.', 'с': '...', 'т': '-', 'у': '..-', 'ф': '..-.', 'х': '....', 'ц': '-.-.',
         'ч': '---.', 'ш': '----', 'щ': '--.-', 'ъ': '--.--', 'ы': '-.--', 'ь': '-..-', 'э': '..-..',
         'ю': '..--', 'я': '.-.-', ' ': '-...-'}

code = input().split() # Пользовательский ввод
result = [] # Зашифрованное сообщение в азбуке Морзе

for symbol in code: # Передаю каждый символ отдельно
    for key, value in morze.items(): # Выбираю ключи и значение из словаря
        if value == symbol: # Сравниваю ключ с символом, оператор in тут не подходит
            print(key, end="") # Печатаю
            break # Сбрасываю итерации так как он будет выводить буквы е, ё. Пример: всеё веёрно

# Если из морзе удалить букву ё
# print(*[morze.get(c) for c in input().split()], sep='')