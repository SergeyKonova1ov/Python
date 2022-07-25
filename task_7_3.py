
import os
import shutil
import sys
from shutil import copy2  # импортируем основные модули для работы с директориями и папками


def main(argv):
    """
    Принимает в качестве аргумента путь к папке со структурой проекта
    и создает в указанной папке папку templates, содержащую все шаблоны проекта
    :param argv: путь к папке со структурой проекта
    :return: создает папку templates, содержащую все шаблоны проекта
    """
    if not os.path.exists(argv[1]): # если директория не существет
        print('Директория не найдена')
        return 1
    for root, dirs, files in os.walk(argv[1]): #проходим по корневой директории с папками и файлами
        print(files)
        if files:
            for f_name in files:
                if f_name.endswith('.html'): # если расширение заканчивается на html
                    src_path = os.path.join(root, f_name)
                    dst_path = os.path.jo  in(argv[1], 'templates', os.path.basename(root), f_name) # задаем путь назначения с папкой templates
                    try:
                        if os.path.exists(dst_path):# если путь назначения существует, возвращаем ошибку
                            raise FileExistsError
                        copy2(src_path, dst_path)#копируем с сохраненем метаданных
                    except FileNotFoundError: # В случае, если возвращается ошибка  "файл не найден"
                        os.makedirs(os.path.dirname(dst_path), exist_ok=True)
                        copy2(src_path, dst_path) #копируем с сохраненем метаданных
                    except (shutil.SameFileError, FileExistsError):
                        if src_path == dst_path:
                            pass
                        else:
                            if input(f'Файл {src_path} уже существует в templates. Копировать с заменой Y/N: ') == 'Y':
                                os.remove(dst_path)
                                copy2(src_path, dst_path)


if __name__ == '__main__':
    sys.exit(main(sys.argv))

