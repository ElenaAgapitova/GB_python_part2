# while True:
#     user_input = input('Введи какой-нибудь текст: ')
#     if user_input == '!!!':
#         break
#     print(type(user_input))
#     print(id(user_input))
#     print(hash(user_input))

# help()

user_input = input('Введи какой-нибудь текст: ')
if user_input.isdigit():
    num = int(user_input)
    print(bin(num))
    print(oct(num))
    print(hex(num))
else:
    print(user_input.isascii())


print(0.1 + 0.2)
