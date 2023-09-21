"""
    Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все
    вложенные директории. Результаты обхода сохраните в файлы json, csv и pickle.
    Для дочерних объектов указывайте родительскую директорию.
    Для каждого объекта укажите файл это или директория.
    Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом
    всех вложенных файлов и директорий.
"""
import csv
import json
import os
import pickle

PATH = 'C:/Users/User/Desktop/Developer/Python_part2/hw_7'


def get_info_about_dirs_and_files(path: str = os.getcwd()):
    file_list = []
    dir_list = []
    for root, dirs, files in os.walk(path):
        for dir_ in dirs:
            dir_path = os.path.join(root, dir_)
            dir_list.append(
                {
                    'dir': dir_path.split('\\')[-2].split('/')[-1],
                    'name': dir_,
                    'type': 'directory',
                    'size': os.path.getsize(dir_path)
                }
            )

        for file in files:
            file_path = os.path.join(root, file)
            file_list.append(
                {
                    'dir': file_path.split('\\')[-2].split('/')[-1],
                    'name': file,
                    'type': 'file',
                    'size': os.path.getsize(file_path)
                }
            )
    return file_list + dir_list


def save_json(info_list: list[dict[str, str | int]]):
    with open('info_json.json', 'w', encoding='utf-8') as js_file:
        json.dump(info_list, js_file, indent=4, ensure_ascii=False)


def save_csv(df_list: list[dict[str, str | int]]):
    with open('info_csv.csv', 'w', newline='', encoding='utf-8') as csv_file:
        columns = ['dir', 'name', 'type', 'size']
        csv_writer = csv.DictWriter(csv_file, dialect='excel', fieldnames=columns)
        csv_writer.writeheader()
        csv_writer.writerows(df_list)


def save_pickle(data_lst: list[dict[str, str | int]]):
    with open('info_pickle.pickle', 'wb') as pickle_file:
        pickle.dump(data_lst, pickle_file)


if __name__ == '__main__':
    info_lst = get_info_about_dirs_and_files(PATH)
    save_json(info_lst)
    save_csv(info_lst)
    save_pickle(info_lst)
