from datetime import datetime


class Data:

    def __init__(self, date: str):
        check = Data.__valid_date(date)
        if check:
            self.date = date

    @classmethod
    def to_int(cls, date: str):
        in_date = cls(date)
        day, month, year = map(int, in_date.date.split('-'))

        return day, month, year

    @staticmethod
    def __valid_date(date):
        try:
            datetime.strptime(date, '%d-%m-%Y')
            return True
        except ValueError:
            raise ValueError('Некорректный формат данных')


if __name__ == '__main__':
    dat = Data('01-01-1987')
    print(dat.to_int('21-08-1987'))