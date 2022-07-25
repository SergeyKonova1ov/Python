class Stationery:

    def __init__(self, title: str) -> None:

        self.title = title

    def draw(self) -> None:

        print('Запись отрисовки')


class Pen(Stationery):

    def draw(self) -> None:

        name = self.__class__.__name__

        if name != 'Pencil':
            print(f'{name}: приступил к отрисовке объекта "{self.title}"')
        else:
            print('Запуск отрисовки')
            print(f'{name}: приступил к отрисовке объекта "{self.title}"')


class Pencil(Stationery):

    def draw(self) -> None:

        name = self.__class__.__name__

        if name != 'Pencil':
            print(f'{name}: приступил к отрисовке объекта "{self.title}"')
        else:
            print('Запуск отрисовки')
            print(f'{name}: приступил к отрисовке объекта "{self.title}"')


class Handle(Stationery):

    def draw(self) -> None:

        name = self.__class__.__name__

        if name != 'Pencil':
            print(f'{name}: приступил к отрисовке объекта "{self.title}"')
        else:
            print('Запуск отрисовки')
            print(f'{name}: приступил к отрисовке объекта "{self.title}"')


if __name__ == '__main__':
    pen = Pen('Ручка')
    pencil = Pencil('Карандаш')
    handle = Handle('Маркер')
    pen.draw()  # Pen: приступил к отрисовке объекта "Ручка"
    handle.draw()  # Handle: приступил к отрисовке объекта "Маркер"
    pencil.draw()  # Пример вывода ниже в многострочном комментарии
    """
    Запуск отрисовки
    Pencil: приступил к отрисовке объекта "Карандаш"
    """