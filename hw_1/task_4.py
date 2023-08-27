# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки.


import random
LOWER_LIMIT = 0
UPPER_LIMIT = 1000
num = random.randint(LOWER_LIMIT, UPPER_LIMIT)

print('Угадай мое число от 0 до 1000!:) У тебя 10 попыток. Поехали...')
count = 10
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


print('Теперь я попытаюсь угадать. Загадай число от 0 до 1000!')
numbers = [i for i in range(UPPER_LIMIT + 1)]
num = numbers[len(numbers)//2]
count = 10

while count != 0:
    user_answer = input(f'Твое число {num} (да/больше/меньше): ')
    if user_answer.lower() == 'да':
        print(f'Ура! Я угадал! Осталось попыток: {count - 1}')
        break
    elif user_answer.lower() == 'больше':
        numbers = numbers[numbers.index(num):]
    elif user_answer.lower() == 'меньше':
        numbers = numbers[:numbers.index(num)]
    num = numbers[len(numbers) // 2]
    count -= 1
