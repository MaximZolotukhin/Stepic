"""
9.2 Функция-генератор. Оператор yield

Подвиг 5. Определите функцию-генератор, которая бы возвращала простые числа.
(Простое число - это натуральное число, которое делится только на себя и на 1).
Выведите с помощью этой функции первые 20 простых чисел (начиная с 2) в одну строчку через пробел.
"""

def is_prime():
    count = 0 # Создаем счетчик чтобы вывести 20 простых чисел
    for i in range(2, 100): # Перебираем до 100 чтобы вложится в 20 чисел и делаем делимое
        div = 0 # Деламе счетчик делителей
        if count < 20: # Пока меньше 20 цикл продолжает работать
            for j in range(2, i+1): # Перебираем делители
                if i % j == 0: # Если после деления остается ноль тогда записываем его в счетчки делителей
                    div +=1
            if div <= 1: # Если делитель 1 тогда это простое число
                count += 1 # Увеличиваем счетчик чисел необходимых для соблюдения 20 символов
                yield i # Возвращаем число
        else:
            break


if __name__ == "__main__":
    val_def = is_prime()
    print(*val_def)