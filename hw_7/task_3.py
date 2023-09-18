#  Напишите функцию группового переименования файлов. Она должна:
# ✔ принимать параметр желаемое конечное имя файлов.
# При переименовании в конце имени добавляется порядковый номер.
# ✔ принимать параметр количество цифр в порядковом номере.
# ✔ принимать параметр расширение исходного файла.
# Переименование должно работать только для этих файлов внутри каталога.
# ✔ принимать параметр расширение конечного файла.
# ✔ принимать диапазон сохраняемого оригинального имени. Например, для диапазона
# [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется
# желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
import os

from task_1 import create_dir_files

for ext in ['.txt', '.pdf', '.py']:
    create_dir_files(ext, dir_='rename_folder', min_size=6, max_size=8, file_count=2)


def group_rename(dir_, wish_name: str = '', num_digits=3, begin_ext: str = '.txt',
                 end_ext: str = '.doc', diapason=None):
    if diapason is None:
        diapason = [3, 6]
    filtered_files = list(filter(lambda x: x.endswith(begin_ext), os.listdir(dir_)))
    for i, item in enumerate(filtered_files, 1):
        name = f'{item[diapason[0] - 1:diapason[1]]}' + \
               f'{wish_name}_' + f'{i:0{num_digits}}' + end_ext
        os.rename(os.path.join(dir_, item), os.path.join(dir_, name))


group_rename('rename_folder', wish_name='_new')
