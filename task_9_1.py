import time


class TrafficLight:
    __color: str

    def running(self):
        dct = {'red': 4, 'yellow': 2, 'green': 3}
        for col, sec in dct.items():
            self.__color = col
            print(self.__color, f'{sec} сек')
            time.sleep(sec)


if __name__ == '__main__':
print(TrafficLight().running())
