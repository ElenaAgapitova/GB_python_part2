# ✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# ✔ Каждая группа включает файлы с несколькими расширениями.
# ✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.
import os
import shutil

FILE_EXTENSIONS = {
    'video': ['.mp4', '.avi', '.mov'],
    'image': ['.jpg', '.png', '.gif'],
    'text': ['.txt', '.doc', '.pdf']
}


def sort_files(name_dir):
    for name in FILE_EXTENSIONS.keys():
        os.makedirs(name, exist_ok=True)

    files = os.listdir(name_dir)
    for file in files:
        extensions = '.' + file.split('.')[1]
        for key, value in FILE_EXTENSIONS.items():
            if extensions in value:
                shutil.move(os.path.join(name_dir, file), os.path.join(key, file))
