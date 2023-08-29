# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки.


import random

LOWER_LIMIT = 0
UPPER_LIMIT = 100
COUNT = 10
num = random.randint(LOWER_LIMIT, UPPER_LIMIT)

print(f'Угадай мое число от {LOWER_LIMIT} до {UPPER_LIMIT}!:) У тебя {COUNT} попыток. Поехали...')
count = COUNT
while count != 0:
    user_num = int(input('Введи свое число: '))
    if user_num == num:
        print(f'Ты угадал! Осталось попыток: {count - 1}')
        break
    elif user_num > num:
        print('Меньше!')
    elif user_num < num:
        print('Больше!')
    count -= 1
else:
    print(f'Ты израсходовал все попытки!  Я загадал - {num}')

# print(f'Теперь я попытаюсь угадать. Загадай число от {LOWER_LIMIT} до {UPPER_LIMIT}!')
# numbers = [i for i in range(UPPER_LIMIT + 1)]
# num = numbers[len(numbers) // 2]
# count = COUNT
#
# while count != 0:
#     user_answer = input(f'Твое число {num} (да/больше/меньше): ')
#     if user_answer.lower() == 'да':
#         print(f'Ура! Я угадал! Осталось попыток: {count - 1}')
#         break
#     elif user_answer.lower() == 'больше':
#         numbers = numbers[numbers.index(num):]
#     elif user_answer.lower() == 'меньше':
#         numbers = numbers[:numbers.index(num)]
#     num = numbers[len(numbers) // 2]
#     count -= 1
# else:
#     print(f'Я израсходовал все попытки! Ты победил!')

print(f'Теперь я попытаюсь угадать. Загадай число от {LOWER_LIMIT} до {UPPER_LIMIT}!')
min_value = LOWER_LIMIT
max_value = UPPER_LIMIT
count = 1

while count <= COUNT:
    num = (min_value + max_value) // 2
    user_answer = input(f'Твое число {num} (да/больше/меньше): ')
    if user_answer.lower() == 'больше':
        min_value = num
    elif user_answer.lower() == 'меньше':
        max_value = num
    elif user_answer.lower() == 'да':
        print(f'Ура! Я угадал! C {count} попытки:)')
        break
    count += 1
else:
    print(f'Я израсходовал все попытки! Ты победил!')