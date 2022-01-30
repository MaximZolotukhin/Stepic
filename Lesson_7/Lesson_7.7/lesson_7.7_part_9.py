"""
7.7 Рекурсивные функции

Великий подвиг 8. Вводится список из целых чисел в одну строчку через пробел.
Необходимо выполнить его сортировку по возрастанию с помощью алгоритма сортировки слиянием.
Функция должна возвращать новый отсортированный список.
Вызовите результирующую функцию сортировки для введенного списка и отобразите результат
на экран в виде последовательности чисел, записанных через пробел.

Подсказка. Для разбиения списка и его последующей сборки используйте рекурсивные функции.

P. S. Теория сортировки в видео предыдущего шага.

Sample Input: 8 11 -6 3 0 1 1
Sample Output: -6 0 1 1 3 8 11
"""

list_in = [int(num) for num in input().split()]


def rec_sort(f_len, s_len):
    """
    Функция слияния с сохранением сортировки
    :param f_len:
    :param s_len:
    :return:
    """
    result_list = [] # сюда будем сохранять знанчения из двух списков по возрастанию
    len_f_len = len(f_len) # Длинна первого списка
    len_s_len = len(s_len) # Длинна второго списка

    i = 0 # Индекс первого списка
    j = 0 # Индекс второго списка

    while i < len_f_len and j < len_s_len: # Пока длинна одного или другова списка меньше счетчкиков
        if f_len[i] <= s_len[j]: # Если знанчение списка f_len[i] меньше или равно s_len[j]
            result_list.append(f_len[i]) # Добавляем его в список result_list
            i += 1 # Увеличиваем счетчки на 1
        elif f_len[i] >= s_len[j]: # Если знанчение списка s_len[j] меньше или равно f_len[i]
            result_list.append(s_len[j]) # Добавляем его в список result_list
            j += 1 # Увеличиваем счетчки на 1
    result_list += f_len[i:] + s_len[j:] # Добавляем оставшиеся элементы в фианальный список result_list
    return result_list


def rec_div(list_in):

    num = len(list_in) // 2 # Получаем число которае будет серидиной массива
    f_len = list_in[:num] # Первая часть массива
    s_len = list_in[num:] # Вторая часть массива
    if len(f_len) > 1: # Если длина f_len больше единицы, то продолжаем делить
        f_len = rec_div(f_len) # Сюда передается список f_len
    if len(s_len) > 1: # Если длина s_len больше единицы, то продолжаем делить
        s_len = rec_div(s_len) # Сюда передается список s_len

    return rec_sort(f_len, s_len) # Слияние двух отсортированных массивов


print(*rec_div(list_in))
