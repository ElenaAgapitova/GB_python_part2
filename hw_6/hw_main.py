from task_1 import check_date
from task_2 import check_position

if __name__ == '__main__':
    # задача №1
    dates = ['45.01.1956', '29.02.2023', '29.02.2024', '23.13.2026',
             '21.05.0000', '09.05.1945', '29.02.2000']
    for i, item in enumerate(dates, 1):
        print(f'{i}. {item} - {check_date(item)}')

    # задача №2
    queens_pos_1 = [(1, 3), (2, 4), (3, 5), (4, 7), (5, 1), (6, 2), (7, 5), (8, 6)]  # False
    queens_pos_2 = [(1, 1), (2, 5), (3, 8), (4, 6), (5, 3), (6, 7), (7, 2), (8, 4)]  # True
    print(check_position(queens_pos_1))
    print(check_position(queens_pos_2))
