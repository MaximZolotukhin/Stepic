"""
6.4 Множества (set) и их методы

Подвиг 4. Вводится текст в одну строку, слова разделены пробелом.
Необходимо подсчитать число уникальных слов (без учета регистра) в этом тексте.
Результат (число уникальных слов) вывести на экран.

Sample Input: Мама мыла раму а потом мыла кота и еще мыла пол

Sample Output: 9
"""
num = set(input().lower().split()) # с помощью input().split() получаю строку и разделяю ее по пробелу
# Перевожу все буквы в нижний регистр с помощью функции lower()
# Все что получил упаковываю в множество с помощью функции set()

print(len(num)) # Вывожу значения в консоль считаю количество элементов