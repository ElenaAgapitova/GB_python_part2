# Напишите однострочный генератор словаря, который принимает
# на вход три списка одинаковой длины: имена str, ставка int,
# премия str с указанием процентов вида «10.25%». В результате
# получаем словарь с именем в качестве ключа и суммой
# премии в качестве значения. Сумма рассчитывается
# как ставка умноженная на процент премии

name = ['Bob', 'Alice', 'Jonn']
rate = [15_000, 25_000, 17_000]
bonus = ['10.25%', '15%', '25%']

dict_gen = ({name[i]: rate[i] * float(bonus[i][:-1])/100} for i in range(len(name)))
print(dict_gen)
print(*dict_gen)
