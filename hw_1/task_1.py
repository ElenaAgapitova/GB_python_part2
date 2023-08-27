# Таблица умножения
START = 2
STOP = 11
STEP = 4

print('\n', '\t' * 5, "ТАБЛИЦА  УМНОЖЕНИЯ\n")

for i in range(START, STOP - 1, STEP):
    for j in range(START, STOP):
        for k in range(i, i + STEP):
            print(f'{k} X {j} = {k * j}', end='\t\t')
        print()
    print()
