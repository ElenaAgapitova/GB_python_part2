# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и
# знаменателем. Программа должна возвращать сумму и произведение* дробей. Для проверки своего
# кода используйте модуль fractions.

from fractions import Fraction
from math import gcd

str_1 = input('Введите первую строку вида a/b: ')
str_2 = input('Введите вторую строку вида a/b: ')

a_1 = int(str_1.split("/")[0])
b_1 = int(str_1.split("/")[1])

a_2 = int(str_2.split("/")[0])
b_2 = int(str_2.split("/")[1])

frac_1 = Fraction(a_1, b_1)
frac_2 = Fraction(a_2, b_2)

print(f'\nПРОВЕРКА\nПроизведение: {frac_1 * frac_2}; сумма: {frac_1 + frac_2}')

# произведение
a, b = a_1 * a_2, b_1 * b_2
a, b = int(a / gcd(a, b)), int(b / gcd(a, b))

# сумма
c, d = a_1 * b_2 + a_2 * b_1, b_1 * b_2
c, d = int(c / gcd(c, d)), int(d / gcd(c, d))

if b != 1 and d != 1:
    result_1 = str(a) + '/' + str(b)
    result_2 = str(c) + '/' + str(d)
elif b == 1 and d != 1:
    result_1 = str(a)
    result_2 = str(c) + '/' + str(d)
elif b != 1 and d == 1:
    result_1 = str(a) + '/' + str(b)
    result_2 = str(c)
else:
    result_1 = str(a)
    result_2 = str(c)

print(f'\nРЕЗУЛЬТАТ\nПроизведение: {result_1}; сумма: {result_2}')
