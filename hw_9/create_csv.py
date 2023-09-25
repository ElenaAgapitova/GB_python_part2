import csv
from random import randint as ri


def create_csv_file(file_name: str = 'parameters.csv', min_row: int = 10, max_row: int = 30, min_value: int = -20,
                    max_value: int = 20):
    count = ri(min_row, max_row)
    params = [[ri(min_value, max_value) for _ in range(3)] for _ in range(count)]
    with open(file_name, 'w', newline='', encoding='utf-8') as file:
        csv_writer = csv.writer(file, dialect='excel')
        csv_writer.writerows(params)


