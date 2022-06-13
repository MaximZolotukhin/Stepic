"""
9.4 Функция filter

Подвиг 5. Вводится список email-адресов в одну строчку через пробел. Среди них нужно оставить
только корректно записанные адреса. Будем полагать, что к таким относятся те, что используют латинские буквы,
цифры и символ подчеркивания. А также в адресе должен быть символ "@", а после него символ точки "."
(между ними, конечно же, могут быть и другие символы).
Результат отобразить в виде строки email-адресов, записанных через пробел.

Sample Input:
abc@it.ru dfd3.ru@mail biba123@list.ru sc_lib@list.ru $fg9@fd.com fg9@fd.com

Sample Output:
abc@it.ru biba123@list.ru sc_lib@list.ru
"""

import string
# letters_and_digits = string.ascii_lowercase + string.digits + '_'
ok_symbols = string.ascii_letters + string.digits + '_'

mail_list = list(input().split())

def mail_valid(val_mail_list):
    ok_symbols = string.ascii_lowercase + string.digits

    if val_mail_list[-3] == '.' or val_mail_list[-4] == '.' and val_mail_list[-5].lower() in ok_symbols and '@' in val_mail_list:
        for val in val_mail_list.lower():
            if val in ok_symbols:
                return True
            else:
                return False
    else:
        return False

    return True


result = filter(mail_valid, mail_list)
print(*result)
