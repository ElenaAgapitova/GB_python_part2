"""
Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код,
решающий задачу о 8 ферзях. Известно, что на доске 8×8 можно расставить 8 ферзей так,
чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске, определите, есть ли
среди них пара бьющих друг друга. Программа получает на вход восемь пар чисел,
каждое число от 1 до 8 - координаты 8 ферзей. Если ферзи не бьют друг друга верните истину, а
если бьют - ложь.

Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной
расстановки ферзей в задаче выше. Проверяйте различный случайные варианты и выведите 4 успешных
расстановки.
"""
import time
from random import randint as ri
from typing import Callable

N = 8


def check_position(position: list[tuple]) -> bool:
    """
    Функция проверяет позиции ферзей, если координаты ферзей совпадают по горизонтали,
    вертикали или диагонали, то они бьют друг друга.
    :param position: список кортежей с позициями ферзей.
    :return: True, если не бьют друг друга, иначе False.
    """
    for i in range(len(position)):
        for j in range(i + 1, len(position)):
            if position[i][0] == position[j][0] or \
                    position[i][1] == position[j][1] or \
                    abs(position[i][0] - position[j][0]) == abs(position[i][1] - position[j][1]):
                return False
    return True


def get_time(func: Callable):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f'Время выполнения: {time.time() - start}')
        return result

    return wrapper


@get_time
def get_good_position(n: int, m: int) -> list[list]:
    """
    Случайный подбор успешных расстановок ферзей.
    :param n: количество ферзей.
    :param m: количество успешных расстановок.
    :return: список 4 удачных расстановок.
    """
    result = []
    while len(result) < m:
        random_position = [(ri(1, 8), ri(1, 8)) for _ in range(n)]
        if check_position(random_position):
            result.append(random_position)
    return result


if __name__ == '__main__':
    for k, item in enumerate(get_good_position(N, 1), 1):
        print(f'{k}.', *item)
