# Создайте функцию генератор чисел Фибоначчи.

from itertools import islice


def get_fibonacci():
    number_1, number_2 = 0, 1
    while True:
        yield number_1
        number_1, number_2 = number_2, number_1 + number_2


print(*islice(get_fibonacci(), 10))
