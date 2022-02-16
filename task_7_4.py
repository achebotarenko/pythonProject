# Написать скрипт, который выводит статистику для заданной папки в виде словаря,
# в котором ключи — верхняя граница размера файла (пусть будет кратна 10),
# а значения — общее количество файлов (в том числе и в подпапках),
# размер которых не превышает этой границы, но больше предыдущей (начинаем с 0), например:
#    {
#     100: 15,
#     1000: 3,
#     10000: 7,
#     100000: 2
#   }
#
# Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...


import os

directory = r'some_data'
files_size = {}
for root, dirs, files in os.walk(os.getcwd()):
    for file in files:
        path = os.path.join(root, file)
        size = os.path.getsize(path)
        dict_keys = (10 ** len(str(size)))
        if dict_keys in files_size:
            files_size[dict_keys] += 1
        else:
            files_size[dict_keys] = 1

keys = list(files_size)
keys.sort()
for dict_keys in keys:
    print(f'{dict_keys}: {files_size[dict_keys]}')
