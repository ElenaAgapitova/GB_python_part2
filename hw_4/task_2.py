# Напишите функцию, принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента. Если ключ не хэшируется,
# используйте его строковое представление.
from pprint import pp


def reverse_dict(**kwargs) -> dict[object, object]:
    """
    Функция, которая принимает на вход только ключевые параметры и возвращает словарь,
    где ключ — значение переданного аргумента, а значение — имя аргумента.
    :param kwargs: любое количество ключевых аргументов.
    :return: словарь.
    """
    reversed_dict = {}
    for key, value in kwargs.items():
        if isinstance(value, (int, float, str, tuple, frozenset)):
            reversed_dict.setdefault(value, key)
        else:
            reversed_dict.setdefault(str(value), key)
    return reversed_dict


pp(reverse_dict(apple=5, манго='mango', coconut=[1, 2, 3, 4],
                pear=(1, 2, 3), banana={'b': 1, 'a': 3, 'n': 2},
                cherry=3.15, pineapple={1, 2, 3, 10}))
