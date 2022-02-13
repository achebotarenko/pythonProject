# Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом  — данные об их хобби.
# Известно, что при хранении данных используется принцип: одна строка — один пользователь,
# разделитель между значениями — запятая. Написать код, загружающий данные из обоих файлов и
# формирующий из них словарь: ключи — ФИО, значения — данные о хобби. Сохранить словарь в файл.
# Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО,
# задаём в словаре значение None. Если наоборот — выходим из скрипта с кодом «1».
# При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.
# Фрагмент файла с данными о пользователях (users.csv):
# Иванов,Иван,Иванович
# Петров,Петр,Петрович

# Фрагмент файла с данными о хобби  (hobby.csv):
# скалолазание,охота
# горные лыжи


import sys
import json

with open('users.csv', 'r', encoding='utf-8') as f:
    surname = []
    for line in f:
        surname.append((line.replace('\n', '').replace(',', ' ')))
with open('hobby.csv', 'r', encoding='utf-8') as f:
    hobby = []
    for line in f:
        hobby.append(line.replace('\n', '').replace(',', ', '))

if len(surname) < len(hobby):
    sys.exit(1)
else:
    for i in range(len(surname)-len(hobby)):
        hobby.append(None)
    dict_hobby = dict(zip(surname, hobby))


with open('surname_hobby.json', 'w', encoding='utf-8') as f:
    dict_hobby_str = json.dumps(dict_hobby)
    f.write(dict_hobby_str)

with open('surname_hobby.json', 'r', encoding='utf-8') as f:
     hobby_surname_str = f.read()
hobby_surname = json.loads(hobby_surname_str)
print(hobby_surname)
