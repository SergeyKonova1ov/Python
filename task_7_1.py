import os # импортируем модуль для работы с файловой системой

path = r'C:/Users/Konovalovs/PycharmProjects/Python' # задаем путь и структуру папок
projectname = 'my_project'
folders = \
    [['settings', []],
     ['mainapp', []],
     ['adminapp', []],
     ['authapp', []]
     ]


def create_folder(path):
    if not os.path.exists(path): # если наша директория не существет, то создать
        os.mkdir(path)


def build(root, data): # создаем структуру папок из заданного списка конфигурации
    if data:
        for d in data:
            name = d[0]
            path = os.path.join(root, name)
            create_folder(path)
            build(path, d[1]) # вызываем функцию еще раз для отслеживания уровня вложенности


fullPath = os.path.join(path, projectname)
create_folder(fullPath)


build(fullPath, folders)
