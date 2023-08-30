# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и
# знаменателем. Программа должна возвращать сумму и произведение* дробей. Для проверки своего
# кода используйте модуль fractions.

from fractions import Fraction
from math import gcd

first_str = list(map(int, input('Введите первую строку вида a/b: ').split('/')))
second_str = list(map(int, input('Введите первую строку вида a/b: ').split('/')))

frac_1 = Fraction(first_str[0], first_str[1])
frac_2 = Fraction(second_str[0], second_str[1])

print(f'\nПРОВЕРКА\nПроизведение: {frac_1 * frac_2}; сумма: {frac_1 + frac_2}')

# произведение
numerator_multi = first_str[0] * second_str[0]
denominator_multi = first_str[1] * second_str[1]
multi_frac = [numerator_multi // gcd(numerator_multi, denominator_multi),
              denominator_multi // gcd(numerator_multi, denominator_multi)]

# сумма
numerator_summ = first_str[0] * second_str[1] + first_str[1] * second_str[0]
denominator_summ = first_str[1] * second_str[1]
summ_frac = [numerator_summ // gcd(numerator_summ, denominator_summ),
             denominator_summ // gcd(numerator_summ, denominator_summ)]

result_1 = f'{multi_frac[0]}/{multi_frac[1]}' if multi_frac[1] != 1 else multi_frac[0]
result_2 = f'{summ_frac[0]}/{summ_frac[1]}' if summ_frac[1] != 1 else summ_frac[0]

print(f'\nРЕЗУЛЬТАТ\nПроизведение: {result_1}; сумма: {result_2}')
