# Верните все возможные варианты комплектации рюкзака.
import itertools

WEIGHT = 8
THINGS = {
    'палатка': 4,
    'спальный мешок': 2,
    'ложка': 0.5,
    'котелок': 3,
    'термос': 1,
}


def find_all_combination(things: dict, weight: int) -> list:
    all_combination = []
    for counter in range(1, len(things.items()) + 1):
        for combination in itertools.combinations(things.items(), r=counter):
            total_weight = sum(weight for _, weight in combination)
            if (weight - min(things.values())) <= total_weight <= weight:
                all_combination.append((total_weight, [thing for thing, _ in combination]))
    return all_combination


possible_combination = sorted(find_all_combination(THINGS, WEIGHT), reverse=True)
print(f'Всего {len(possible_combination)} варианта/ов c максимально возможным весом:')
for i, item in enumerate(possible_combination, 1):
    print(f'{i}. {item[0]} кг', end=' ')
    print(*item[1], sep=', ')
