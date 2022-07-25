from abc import abstractmethod

class Clothes:
    @abstractmethod
    def calculate(self):
        pass

class Coat(Clothes):
    def __init__(self, size: float):
        self.size = size

    @property
    def calculate(self):
        cons = self.size / 6.5 + 0.5
        return round(cons, 2)

class Costume(Clothes):
    def __init__(self, height: float):
        self.height = height

    @property
    def calculate(self):
        cons = self.height * 2 + 0.3
        return round(cons, 2)

class Costume2(Clothes):
    def __init__(self, height: float):
        self.height = height

if __name__ == '__main__':
    coat = Coat(45.0)
    costume = Costume(3)
    costume2 = Costume2(3)
    print(coat.calculate)  # 7.42
    print(costume.calculate)  # 6.3