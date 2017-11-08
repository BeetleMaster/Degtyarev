
"""Дан файл, которые содержит в себе пути до файлов, расположенных на жестком
диске. Написать скрипт, который создает резервные копии этих файлов и 
складывает их в отдельную директорию, при этом приведите название файлов к виду: 
<название папки откуда взяли файл>_<оригинальное название файла>.<расширение>
"""


import os
import shutil

count = 0

with open('new_path.txt', 'r') as d:
    directory = d.readline()
    if not os.path.exists(directory):
        os.makedirs(directory)

with open('path.txt', 'r') as f:
    data = f.read().split()
    if not data:
        print('Файл пуст')

    for i in data:
        try:
            file_path = os.path.split(i)
            file_name = file_path[-1]
            directory_name = os.path.split(file_path[0])
            new_path = os.path.join(directory, directory_name[-1]+'_'+file_name)
            shutil.copy(i, new_path, follow_symlinks=True)
        except (FileNotFoundError, IOError):
            count += 1
            
print('Копирование выполнено')
print('Количество неверных путей =', count)
