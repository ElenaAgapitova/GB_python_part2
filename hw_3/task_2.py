# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.
import random

first_list = [random.randint(0, 10) for _ in range(10)]
print(first_list)

second_list = []

for item in set(first_list):
    if first_list.count(item) != 1:
        second_list.append(item)

print(second_list)
