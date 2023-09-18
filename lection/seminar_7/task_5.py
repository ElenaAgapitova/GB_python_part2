# ✔Доработаем предыдущую задачу.
# ✔Создайте новую функцию которая генерирует файлы с разными расширениями.
# ✔Расширения и количество файлов функция принимает в качестве параметров.
# ✔Количество переданных расширений может быть любым.
# ✔Количество файлов для каждого расширения различно.
# ✔Внутри используйте вызов функции из прошлой задачи.
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


def func_2(extensions: tuple[str], file_count: int):
    for _ in range(file_count):
        extension = rnd.choice(extensions)
        func(extension, file_count=1)


func_2(('.txt', '.bmp', '.jpg', '.mp3'), 6)
