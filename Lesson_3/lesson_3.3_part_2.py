"""
3.3 Основные методы строк

Подвиг 3. Вводится строка. Необходимо определить число вхождений дефисов (-) в этой строке.
На экране отобразить полученное число.

Sample Input: osnovnye-metody-strok
Sample Output: 2
"""
# Сохраняю данные в переменную
word = input()
# С помощью метода count('-') - считаю сколько раз в строке встречается символ переданный аргументом.
print(word.count('-'))
