"""
6.2 Методы словаря. Перебор его элементов в цикле
Подвиг 7. Имеется словарь с наименованиями предметов и их весом (в граммах):

things = {'карандаш': 20, 'зеркальце': 100, 'зонт': 500, 'рубашка': 300,
          'брюки': 1000, 'бумага': 200, 'молоток': 600, 'пила': 400, 'удочка': 1200,
          'расческа': 40, 'котелок': 820, 'палатка': 5240, 'брезент': 2130, 'спички': 10}

Сергей собирается в поход и готов взвалить на свои хрупкие плечи максимальный вес в N кг (вводится с клавиатуры).
Он решил класть в рюкзак предметы в порядке убывания их веса (сначала самые тяжелые, затем, все более легкие) так,
чтобы их суммарный вес не превысил значения N кг. Все предметы даны в единственном экземпляре.
Выведите список предметов (в строчку через пробел), которые берет с собой Сергей в порядке убывания их веса.

P. S. 1 кг = 1000 грамм

Sample Input: 10

Sample Output: палатка брезент удочка брюки пила карандаш спички
"""

things = {'карандаш': 20, 'зеркальце': 100, 'зонт': 500, 'рубашка': 300,
          'брюки': 1000, 'бумага': 200, 'молоток': 600, 'пила': 400, 'удочка': 1200,
          'расческа': 40, 'котелок': 820, 'палатка': 5240, 'брезент': 2130, 'спички': 10}

weidth = int(input()) * 1000 # Сохраняю пользовательский ввод сразу его перевожу в граммы
weidth_in_backpack = sorted([inventory for inventory in things.values()], reverse=True) # Беру все значения из списка и
# сортирую их по возрастанию

inventory_in_way = [] # Создаю список значений которые возьмем с собой
for i in range(len(weidth_in_backpack)): # Прохожу по сортированному списку выбираю 1 значение
    for key, val in things.items(): # Прохожу по словарю
        if weidth - val >= 0: # Если отнять значение от основного списка и оно не будет меньше нуля
            if val == weidth_in_backpack[i]: # Проверяю советует ли значение вес, весу объекта
                # print(key, end=' ')
                inventory_in_way.append(key) # Если да то сохраняю его в список
                weidth -= val # Отнимаю вес от общего веса, чтобы бы узнать оставшийся все
                break # Прерываю работу цикла для нового прохода по словарю

print(*inventory_in_way)


# -------------------------------    Вариант не мой --------------------------------------------
# things = {'карандаш': 20, 'зеркальце': 100, 'зонт': 500, 'рубашка': 300,
#           'брюки': 1000, 'бумага': 200, 'молоток': 600, 'пила': 400, 'удочка': 1200,
#           'расческа': 40, 'котелок': 820, 'палатка': 5240, 'брезент': 2130, 'спички': 10}
#
# N = float(input()) * 1000
#
# list_sorted = sorted(things.items(), key = lambda item: item[1], reverse = True) # Сортировка значений в списке.
#
# things = {key: value for key, value in list_sorted} # Сортировка значений в словаре.
#
# for item, weight in things.items():
#     if N - weight >= 0:
#         print(item, end = ' ')
#         N = N - weight
#     else:
#         continue