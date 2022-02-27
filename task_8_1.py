# Написать функцию email_parse(<email_address>), которая при помощи
# регулярного выражения извлекает имя пользователя и почтовый домен
# из email адреса и возвращает их в виде словаря.
# Если адрес не валиден, выбросить исключение ValueError. Пример:
# >>> email_parse('someone@geekbrains.ru')
# {'username': 'someone', 'domain': 'geekbrains.ru'}
# >>> email_parse('someone@geekbrainsru')
# Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#  ...
#    raise ValueError(msg)
# ValueError: wrong email: someone@geekbrainsru

import re


def email_parse(email_address):
    parsed = re.findall(r'(^[a-zA-Z0-9\.\_\-]+)@([a-zA-Z0-9)]+\.[a-zA-Z\.]{2,}$)', email_address)
    if not parsed:
        raise ValueError(f'wrong email: {email_address}')
    return dict(zip(["username", "domain"], parsed[0]))


print(email_parse('support@support.com'))
print(email_parse('sale@trade.com'))
print(email_parse('info@business.au'))
print(email_parse('tech_support@life.com.by'))
print(email_parse('billing.free@tv.io'))
print(email_parse('firs@line@support.info'))  # return ValueError: wrong email
