"""
Напишите следующие функции:
Нахождение корней квадратного уравнения
Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел
из csv файла.
Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
"""

import csv
import json
import os.path
from typing import Callable

from create_csv import create_csv_file


def csv_decor(func: Callable):
    def wrapper(params_file='parameters.csv'):
        result_dict = {}
        if os.path.isfile(params_file):
            with open(params_file, 'r', encoding='utf-8') as file:
                csv_reader = csv.reader(file, dialect='excel')
                for line in csv_reader:
                    a, b, c = (list(map(int, line)))
                    result_dict[f'Параметры: {a=}, {b=}, {c=}'] = func(a, b, c)
        return result_dict

    return wrapper


def json_decor(filename: str = 'result.json'):
    def decor(func: Callable):
        def wrapper(*args):
            result = func(*args)
            with open(filename, 'w', encoding='utf-8') as file:
                json.dump(result, file, indent=4, ensure_ascii=False)
            return result

        return wrapper

    return decor


@json_decor()
@csv_decor
def solved_equation(a: int, b: int, c: int) -> float | tuple | str:
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return 'Корней нет'
    elif discriminant == 0:
        return round((-b) / 2 * a, 3)
    return round((-b - discriminant ** 0.5) / 2 * a, 3), round((-b + discriminant ** 0.5) / 2 * a, 3)


if __name__ == '__main__':
    create_csv_file()
    print(solved_equation())
