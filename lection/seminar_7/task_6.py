# ✔Дорабатываем функции из предыдущих задач.
# ✔Генерируйте файлы в указанную директорию — отдельный параметр функции.
# ✔Отсутствие/наличие директории не должно вызывать ошибок в работе функции (добавьте проверки).
# ✔Существующие файлы не должны удаляться/изменяться в случае совпадения имён.

import os
import random as rnd
import string


def func(extension: str, dir: str = '', min_size: int = 6, max_size: int = 30, min_count: int = 256,
         max_count: int = 4096,
         file_count: int = 42):
    letters = string.ascii_lowercase

    if dir:
        if not os.path.isdir(dir):
            os.mkdir(dir)

    for _ in range(file_count):
        name_size = rnd.randint(min_size, max_size)
        name = rnd.choices(letters, k=name_size)
        name = ''.join(name)

        if os.path.isfile(os.path.join(dir, name + extension)):
            x = 1
            while os.path.isfile(os.path.join(dir, name + f'_{x}' + extension)):
                x += 1
            file_name = name + f'_{x}' + extension
        else:
            file_name = ''.join(name) + extension

        rnd_size = rnd.randint(min_count, max_count)
        data = rnd.randbytes(rnd_size)

        with open(os.path.join(dir, file_name), 'wb') as file:
            file.write(data)


func('.txt', dir='new_bin', min_size=1, max_size=2, file_count=100)
