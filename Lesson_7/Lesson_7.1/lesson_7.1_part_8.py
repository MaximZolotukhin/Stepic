"""
7.1 Что такое функции. Их объявление и вызов

Подвиг 8. Напишите функцию, которая проверяет корректность переданного ей email-адреса в виде строки.
Будем полагать, что адрес верен, если он обязательно содержит символы '@' и '.', а все остальные символы
могут принимать значения: 'a-z', 'A-Z', '0-9' и '_'. Если email верен, то функция выводит ДА, иначе - НЕТ.
После объявления функции прочитайте (с помощью функции input) строку с email-адресом и
вызовите функцию с этим аргументом.

Sample Input: sc_lib@list.ru
Sample Output: ДА
"""


def email_correct_test(e_mail):
    """
    Функция, которая проверяет корректность переданного ей email-адреса
    :param e_mail: Переданный пользователем e-mail
    :test_symbol: Набор символов для проверки e-mail,а
    :flag: Переменная для хранения ответа от цикла имеет два значения ДА или НЕТ
    :return: Выводит в консоль ДА если email-адрес корректен, иначе выводи НЕТ
    """

    test_symbol = {'A', 'E', 'I', 'O', 'U', 'Y', 'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R',
                   'S', 'T',
                   'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '_', 'a', 'e', 'i', 'o',
                   'u', 'y',
                   'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y',
                   'z', '@',
                   '.'}
    flag = ''
    # Цикл посимвольно проверяет наличие каждого символа в тестовой таблице
    for val in e_mail:
        if val in test_symbol:
            flag = "ДА"
        else:
            flag = "НЕТ"
            break

    print(flag)


e_mail = input()  # Запрос на ввод адреса электронной почты
email_correct_test(e_mail)
