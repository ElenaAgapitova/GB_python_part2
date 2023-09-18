# ✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# ✔ Каждая группа включает файлы с несколькими расширениями.
# ✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.
import os
import shutil

from task_1 import create_dir_files

FILE_EXTENSIONS = {
    'video': ['.mp4', '.avi', '.mov'],
    'image': ['.jpg', '.png', '.gif'],
    'text': ['.txt', '.doc', '.pdf']
}

for ext_list in FILE_EXTENSIONS.values():
    for ext in ext_list:
        create_dir_files(ext, dir_='mix_folder', min_size=4, max_size=6, file_count=1)

create_dir_files('.py', dir_='mix_folder', min_size=4, max_size=6, file_count=3)


def sort_files(name_dir):
    for name in FILE_EXTENSIONS.keys():
        os.makedirs(name, exist_ok=True)

    files = os.listdir(name_dir)
    for file in files:
        extensions = '.' + file.split('.')[1]
        for key, value in FILE_EXTENSIONS.items():
            if extensions in value:
                shutil.move(os.path.join(name_dir, file), os.path.join(key, file))


if __name__ == '__main__':
    sort_files('mix_folder')
