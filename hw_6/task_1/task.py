"""
Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате
DD.MM.YYYY Функция возвращает истину, если дата может существовать или ложь, если
такая дата невозможна. Для простоты договоримся, что год может быть в диапазоне [1, 9999].
Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
Проверку високосного года вынести в отдельную защищённую функцию.

В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.
"""
from sys import argv

_month_dict = {
    "01": 31,
    "02": [28, 29],
    "03": 31,
    "04": 30,
    "05": 31,
    "06": 30,
    "07": 31,
    "08": 31,
    "09": 30,
    "10": 31,
    "11": 30,
    "12": 31
}


def _check_leap_year(year: int) -> bool:
    """
    Проверяет високосный год или нет.
    :param year: значение года.
    :return: истину, если год високосный, иначе - ложь.
    """
    if not year % 400:
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True
    return False


def check_date(user_date: str) -> bool:
    """
    Проверка даты.
    :param user_date: дата в формате DD.MM.YYYY.
    :return: возвращает истину, если дата может существовать или ложь, если
    такая дата невозможна.
    """
    date_list = user_date.split('.')
    if date_list[1] in _month_dict.keys() and 1 <= int(date_list[2]) <= 9999:
        if date_list[1] != '02':
            return 1 <= int(date_list[0]) <= _month_dict.get(date_list[1])
        else:
            if _check_leap_year(int(date_list[2])):
                return 1 <= int(date_list[0]) <= _month_dict['02'][1]
            else:
                return 1 <= int(date_list[0]) <= _month_dict['02'][0]
    return False


if __name__ == '__main__':
    date = argv[1:]
    if date:
        print(date[0], check_date(date[0]))
