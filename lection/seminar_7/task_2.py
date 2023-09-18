# ✔Напишите функцию, которая генерирует псевдоимена.
# ✔Имя должно начинаться с заглавной буквы, состоять из 4-7 букв,
# среди которых обязательно должны быть гласные.
# ✔Полученные имена сохраните в файл.

import random as rnd
import string

VOWELS = {'a', 'e', 'i', 'o', 'u', 'y'}
CONSONANTS = set(string.ascii_lowercase) - VOWELS


def generate_name():
    size = rnd.randint(4, 7)
    name = ''
    for i in range(size):
        name += rnd.choice(list(VOWELS)) if i % 2 else rnd.choice(list(CONSONANTS))
    return name.title()


def write_names_to_file(filename: str, count: int):
    with open(filename, 'a+', encoding='UTF-8') as file:
        for _ in range(count):
            file.write(f'{generate_name()}\n')


write_names_to_file('task_2_file.txt', 10)
