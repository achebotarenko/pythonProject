# Создать структуру файлов и папок, как написано в задании 2
# (при помощи скрипта или «руками» в проводнике).
# |--my_project
#    |--settings
#    |  |--__init__.py
#    |  |--dev.py
#    |  |--prod.py
#    |--mainapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--mainapp
#    |        |--base.html
#    |        |--index.html
#    |--authapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |  |   | --authapp
#    |         | --base.html
#    |         | --index.html

# Написать скрипт, который собирает все шаблоны в одну папку templates, например:
# |--my_project
#   ...
#   |--templates
#   |   |--mainapp
#   |   |  |--base.html
#   |   |  |--index.html
#   |   |--authapp
#   |      |--base.html
#   |      |--index.html


import os
import shutil

with open('path_7_3.txt', 'r') as f:
    for row in f.read().splitlines():
        if not os.path.exists(row) and not row.lower().__contains__('.'):
            os.mkdir(row)
        elif row.lower().__contains__('.'):
            with open(row, 'w') as new_file:
                new_file.write("")

main_dir = 'my_project'
result_dir = 'my_project\\templates'
for dir_path, dir_name, file_names in os.walk(main_dir):
    if dir_path.split('\\')[-1] == 'templates':
        for dirs in dir_name:
            src = os.path.join(dir_path, dirs)
            dst = os.path.join(result_dir, dirs)
            if not os.path.exists(dst):
                shutil.copytree(src, dst)
