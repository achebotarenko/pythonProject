# Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
# |--my_project
#   |--settings
#   |--mainapp
#   |--adminapp
#   |--authapp
#
# Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?);
# как лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена папок
# под конкретный проект; можно ли будет при этом расширять конфигурацию и хранить данные о вложенных
# папках и файлах (добавлять детали)?


import os

main_dir = 'my_project'
sub_dir = ['settings', 'mainapp', 'adminapp', 'authapp']

if not os.path.exists(main_dir):
    os.mkdir(main_dir)
[os.makedirs(os.path.join(main_dir, folder)) for folder in sub_dir
 if not os.path.exists(os.path.join(main_dir, folder))]

with open('paths.txt', 'w') as f:
    f.writelines([main_dir, '\n'])
    [f.writelines([os.path.join(main_dir, folder), '\n']) for folder in sub_dir]
