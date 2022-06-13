"""
7.11 Декораторы функций

Подвиг 5. Объявите функцию, которая принимает строку на кириллице и преобразовывает ее в латиницу,
используя следующий словарь для замены русских букв на соответствующее латинское написание:

t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}

Функция должна возвращать преобразованную строку. Замены делать без учета регистра (исходную строку перевести
в нижний регистр - малые буквы). Все небуквенные символы ": ;.,_" превращать в символ '-' (дефиса).
Определите декоратор для этой функции, который несколько подряд идущих дефисов, превращает в один дефис.
Полученная строка должна возвращаться при вызове декоратора. (Сам декоратор на экран ничего выводить не должен).
Примените декоратор к первой функции и вызовите ее для введенной строки s на кириллице:

s = input()

Результат работы декорированной функции отобразите на экране.

Sample Input: Python - это круто!
Sample Output: python-eto-kruto!
"""
t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}

string = input()

def translite(any_func):
    def wrapper(*args, **kwargs):
        res = any_func(*args, **kwargs)
        res = res.replace("---", "-")
        res = res.replace("--", "-")
        return res
    return wrapper


@translite
def string_lower(string, t):
    result = ''
    for val in string.lower(): # Вытаскиваем один символ из пользовательской строки
        if val in t:
            for key, value in t.items(): # Сравниваем символ с таблицей кодировки
                if val == key: # Если да то сохраняем символ из таблицы кодировки в строку
                    result += value
        elif  val not in t.keys() and val not in ": ;.,_":
            result += val
        elif val in ": ;.,_": # Если да то заменяем пробел на необходимую строку.
            result += '-'

    return result


print(string_lower(string, t))