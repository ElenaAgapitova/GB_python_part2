# Верните все возможные варианты комплектации рюкзака.
import itertools

WEIGHT = 8
THINGS = {
    'Палатка': 4,
    'Спальный мешок': 2,
    'Ложка': 0.5,
    'Котелок': 3,
    'Термос': 1
}

all_combination = []
for i in range(1, len(THINGS.items()) + 1):
    for combination in itertools.combinations(THINGS.items(), r=i):
        total_weight = sum(weight for _, weight in combination)
        if total_weight <= WEIGHT:
            all_combination.append([thing for thing, _ in combination])

for i, item in enumerate(all_combination, 1):
    print(f'Вариант {i}.', end=' '),
    print(*item, sep=', ')
