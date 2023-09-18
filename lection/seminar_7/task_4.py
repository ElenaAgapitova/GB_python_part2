# ✔Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры: ✔расширение ✔минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔количество файлов, по умолчанию 42
# ✔Имя файла и его размер должны быть в рамках переданного диапазона.
import os
import random as rnd
import string


def func(extension: str, min_size: int = 6, max_size: int = 30, min_count: int = 256, max_count: int = 4096,
         file_count: int = 42):
    letters = string.ascii_lowercase
    for _ in range(file_count):
        name_size = rnd.randint(min_size, max_size)
        file_name = rnd.choices(letters, k=name_size)
        file_name = ''.join(file_name) + extension

        rnd_size = rnd.randint(min_count, max_count)
        data = rnd.randbytes(rnd_size)

        os.makedirs('bin', exist_ok=True)
        with open(os.path.join('bin', file_name), 'wb') as file:
            file.write(data)


func('.txt', file_count=3)
