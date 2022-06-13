"""
9.2 Функция-генератор. Оператор yield

Подвиг 2. Мы с вами в заданиях несколько раз генерировали последовательность чисел Фибоначчи, которая строится по
правилу: каждое последующее число равно сумме двух предыдущих. Для разнообразия давайте будем генерировать каждое
последующее как сумму трех предыдущих чисел. При этом первые три числа равны 1 и имеем такую последовательность:
1, 1, 1, 3, 5, 9, 17, 31, 57, ...
Не знаю, есть ли у нее название, поэтому, в рамках уроков, я скромно назову ее последовательностью Балакирева.

Итак, на вход программы поступает натуральное число N (N > 5) и необходимо определить функцию-генератор,
которая бы возвращала N первых чисел последовательности Балакирева (включая первые три единицы).

Реализуйте эту функцию без использования коллекций (списков, кортежей, словарей и т.п.).
Вызовите ее N раз для получения N чисел и выведите полученные числа на экран в одну строчку через пробел.

Sample Input: 7
Sample Output: 1 1 1 3 5 9 17
"""
# ввод значения N (эту переменную не менять)
N = int(input())

# здесь продолжайте программу

def get_sum(N):
    sum = [1, 1, 1] # Число которое будет сохранять сумму
    result = 0
    for val in range(2, N-1): # Цикл где мы получем число от 1 до N+1
        result = sum[-1] + sum[-2] + sum[-3]
        sum.append(result) # Суммирование полученных чисел
    return sum # Ставим на паузу выплнение цикла и возвращаем полученное число

if __name__ == "__main__":
    val_def = get_sum(N)
    print(*val_def)

