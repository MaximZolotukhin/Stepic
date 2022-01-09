"""
5.8 Генераторы списков (List comprehension)

Подвиг 3. Вводится натуральное число N. С помощью list comprehension сформировать двумерный список размером N x N,
состоящий из нулей, а по главной диагонали - единицы. (Главная диагональ - это элементы,
идущие по диагонали от верхнего левого угла матрицы до ее нижнего правого угла).
Результат вывести в виде таблицы чисел как показано в примере ниже.

Sample Input: 4
Sample Output:
1 0 0 0
0 1 0 0
0 0 1 0
0 0 0 1
"""
# Как решил я первый раз
size_matrix = int(input()) # Пользовательский ввод
matrix = [(1 if x == i else 0) for i in range(0, size_matrix) for x in range(0, size_matrix)] # Если x  равна i тогда
# печатаем 1 иначе 0, дальне циклом заполняем все необходимыми цифрами до заданного пользователем размера

count = 1 # Создаю счетчик
for i in matrix: # Прохожу по полученному списку
    if count % size_matrix == 0: # Если остаток от деления равен 0
        print(i)    # тогда вывожу число без пробела и с переносом на новую строку
    else:
        print(i, end=" ") # Иначе вывожу с пробелом и оставляю на этой строке
    count += 1 # Увеличиваю счетчик на 1

# Более правильное решение
# print("----------------------------------------------------------------------------------")
# matrix_2 = [[1 if x == i else 0 for i in range(size_matrix)] for x in range(size_matrix)]
# for i in matrix_2:
#     print(*i)
