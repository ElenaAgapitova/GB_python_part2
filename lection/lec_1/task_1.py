# while True:
#     user_input = input('Введи какой-нибудь текст: ')
#     if user_input == '!!!':
#         break
#     print(type(user_input))
#     print(id(user_input))
#     print(hash(user_input))

# help()

# user_input = input('Введи какой-нибудь текст: ')
# if user_input.isdigit():
#     num = int(user_input)
#     print(bin(num))
#     print(oct(num))
#     print(hex(num))
# else:
#     print(user_input.isascii())
#
#
# print(0.1 + 0.2)

# my_tuple = (2, 4, 6, 2, 8, 10, 12, 14, 16, 18)
# print(my_tuple[2:6:2])
# print(my_tuple[-3])
# print(my_tuple.count(2))
# print(f'{my_tuple = }')
# print(my_tuple.index(2, 2))
# print(type('text',))

# my_dict = {'one': 1, 'two': 2, 'three': 3}
#
# for i in my_dict:
#     print(i)

a = 'hello world'  # неизменяемый объект (также к ним относятся кортеж, frozenset, числа)
b = [1, 2, 3, 5]  # изменяемый объект (также к ним относятся словари, множества)
# изменяемые объекты не хэшируемые
# print(hash(a))  # -6180989516210485593
# print(hash(b)) TypeError: unhashable type: 'list'

c = list(range(0, 10, 2))
# print(c)

my_gen = (key*2 for key in b)
d = set(my_gen)
print(d)

