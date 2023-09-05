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


def find_all_combination(things: dict, weight: int) -> list:
    all_combination = []
    for counter in range(1, len(things.items()) + 1):
        for combination in itertools.combinations(things.items(), r=counter):
            total_weight = sum(weight for _, weight in combination)
            if total_weight <= weight:
                all_combination.append([thing for thing, _ in combination])
    return all_combination


possible_combination = find_all_combination(THINGS, WEIGHT)
print(f'Всего {len(possible_combination)} возможных комбинаций:')
for i, item in enumerate(possible_combination, 1):
    print(f'{i}.', end=' '),
    print(*item, sep=', ')
