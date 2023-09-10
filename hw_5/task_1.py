# Создайте функцию-генератор.
# ✔ Функция генерирует N простых чисел,
# начиная с числа 2.
# ✔ Для проверки числа на простоту используйте
# правило: «число является простым, если делится
# нацело только на единицу и на себя».

def is_prime(num):
    del_ = 2
    while del_ ** 2 < num and num % del_ != 0:
        del_ += 1
    return del_ ** 2 > num


def gen_is_prime(number):
    """Генератор простых чисел от 2 до n"""
    start = 1
    while number > 1:
        start += 1
        number -= 1
        if is_prime(start):
            yield start


print(*gen_is_prime(100))
