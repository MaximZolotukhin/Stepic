"""
4.2 Вложенные условия и множественный выбор

Подвиг 3. Вводится вес боксера-любителя (в кг, в виде вещественного числа).
Известно, что вес таков, что боксер может быть отнесен к одной из весовых категорий:
1) легкий вес – до 60 кг (включительно);
2) первый полусредний вес – до 64 кг (включительно);
3) полусредний вес – до 69 кг (включительно);
4) остальные - более 69 кг.

Вывести на экран номер категории, в которой будет выступать боксер.
Sample Input: 62.4
Sample Output: 2
"""

# Сохраняю данные в переменную
width = float(input())
# Выполняю проверку согласно условию
if width <= 60:
    print('1')
elif width > 60 and width <= 64:
    print('2')
elif width > 64 and width <= 69:
    print('3')
elif width > 69:
    print('4')
else:
    print('Такой пункт меню отсутствует')
