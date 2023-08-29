# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex используйте для проверки своего результата.

BASE = 16
LETTER_DICT = {10: "a", 11: "b", 12: "c", 13: "d", 14: "e", 15: "f"}

original_number = int(input('Введите число: '))
number = original_number
result_number = ''

while number:
    div_remainder = number % BASE
    if LETTER_DICT.get(div_remainder):
        result_number = LETTER_DICT.get(div_remainder) + result_number
    else:
        result_number = str(div_remainder) + result_number
    number //= BASE

print(f'Результат: {result_number}\nПроверка: {hex(original_number)[2::]}')
