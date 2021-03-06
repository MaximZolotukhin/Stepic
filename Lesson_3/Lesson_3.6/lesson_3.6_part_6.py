"""
3.6 Списки и операции над ними

Подвиг 9. Вводится число новых подписчиков канала по дням в одну строку через пробел.
На основе введенной строки необходимо сформировать список из целых чисел.
Затем, вывести на экран максимальное, минимальное и суммарное значения этого списка через пробел.

Sample Input: 52 65 64 54 68 59 42 63
Sample Output: 68 42 467
"""

# Сохраняем данные в перемененную
people = list(map(int, input().split()))
# Выводим максимальное, минимальное значения и сумму числе в списке
print(f"{max(people)} {min(people)} {sum(people)}")
