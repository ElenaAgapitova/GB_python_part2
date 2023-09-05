"""
Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей.
Ответьте на вопросы:
✔ Какие вещи взяли все три друга
✔ Какие вещи уникальны, есть только у одного друга
✔ Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
✔ Для решения используйте операции с множествами. Код должен расширяться на любое большее количество
друзей.
"""
from collections import Counter

FRIENDS = {
    'Андрей': ('Палатка', 'Спальный мешок', 'Термос'),
    'Мария': ('Котелок', 'Термос', 'Ложка'),
    'Иван': ('Палатка', 'Ложка', 'Термос'),
    'Наталья': ('Нож', 'Палатка', 'Термос'),
}

# Какие вещи взяли все друзья - 1 способ:

common_things = set(FRIENDS[next(iter(FRIENDS))])
for value in FRIENDS.values():
    common_things = common_things.intersection(value)
print('Есть у всех друзей:',  *common_things)

# Какие вещи взяли все три друга - 2 способ
# Какие вещи уникальны, есть только у одного друга
# Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует

all_things = Counter(thing for things in FRIENDS.values() for thing in things)
names = set(FRIENDS.keys())
find_friends = set()
find_thing = None
thing_all_friends = None

for key, value in FRIENDS.items():
    for thing in value:
        if all_things.get(thing, 0) == 1:
            print(f'{thing} есть только у {key}')
        elif all_things.get(thing, 0) == len(FRIENDS) - 1:
            find_thing = thing
            find_friends.add(key)
        elif all_things.get(thing, 0) == len(FRIENDS):
            thing_all_friends = thing

if find_thing is not None:
    print(f'{find_thing} нет у', *(names - find_friends))

if thing_all_friends is not None:
    print(f'{thing_all_friends} есть у всех друзей')
