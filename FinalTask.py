
"""Дан файл, которые содержит в себе пути до файлов, расположенных на жестком
диске. Написать скрипт, который создает резервные копии этих файлов и 
складывает их в отдельную директорию, при этом приведите название файлов к виду: 
<название папки откуда взяли файл>_<оригинальное название файла>.<расширение>
"""


import os
import shutil

with open('new_path.txt', 'r') as d:
    directory = d.readline()
    new_dir = str(directory)
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)

with open('path.txt', 'r') as f:
    data = f.read().split()
    if not data:
        print('Файл пуст')
    for i in data:
        if '/' in i:
            old_name = i.split('/')
            new_name = old_name[-1]
            old_path = i.split('/')
            filter_path = list(filter(None, old_path))
            path_name = filter_path[-2] + '_'
            shutil.copy(i, new_dir + path_name + new_name, follow_symlinks=True)
        else:
            old_name = i.split('\\')
            new_name = old_name[-1]
            old_path = i.split('\\')
            filter_path = list(filter(None, old_path))
            path_name = filter_path[-2] + '_'
            shutil.copy(i, new_dir + path_name + new_name, follow_symlinks=True)
print('Копирование выполнено')
