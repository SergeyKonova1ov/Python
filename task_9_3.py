class Worker:

    def __init__(self, name: str, surname: str, position: str, income: dict):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income

class Position(Worker):

    def get_full_name(self) -> str:
        """Возвращает строку по формату 'Имя Фамилия'"""

        return f'{self.name.lower().capitalize()} {self.surname.lower().capitalize()}'

    def get_total_income(self) -> int:
        """Возвращает суммарный ежемесячных доход"""

        return sum(self._income.values())


if __name__ == '__main__':
    taxi = Position('александр', 'иванов', 'таксист', {'wage': 35000, 'bonus': 10000})
    cleaner = Position('елена', 'петровна', 'уборщик', {'wage': 10000, 'bonus': 2500})
    topmanager = Position('петр', 'алексеев', 'директор', {'wage': 200000, 'bonus': 50000})
    print(taxi.get_full_name(), taxi.get_total_income())  # сумма оклад + премия = 45000
    print(cleaner.get_full_name(), cleaner.get_total_income())  # сумма оклад + премия = 12500
    print( topmanager.get_full_name(),  topmanager.get_total_income())   # сумма оклад + премия = 250000