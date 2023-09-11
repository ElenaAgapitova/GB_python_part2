# Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла
import os
from typing import Any

str_ = 'C:/Users/User/Desktop/Developer/FinalControl/linux.pdf'


def split_path_1(txt):
    *a, b = txt.split('/')
    return '/'.join(a), *b.split('.')


def split_path_2(path: str) -> tuple[str, Any]:
    return os.path.split(path)[0], *os.path.split(path)[1].split('.')


print(split_path_1(str_))
print(split_path_2(input('Введите путь к файлу: ')))
