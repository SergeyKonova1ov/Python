from functools import wraps


def check_arg(*argv):  # Функция (аргумент декоратора), проверяющая аргументы декорируемой функции
    if len(argv) != 1:
        msg = f'wrong val {argv}'
        raise ValueError(msg)
    if not isinstance(argv[0], int) or argv[0] <= 0:  # isinstance определяет принадлежность аргумента к классу int
        msg = f'wrong val {argv[0]}'
        raise ValueError(msg)


def val_checker(func):   # Декоратор
    def _val_checker(main_func):
        @wraps(main_func)  # Маскировка декоратора
        def wrapper(*args):
            func(*args)  # Вызов функции check_arg с аргументом функции calc_cube
            result = main_func(*args)  # Результат выполнения функции calc_cube
            return result
        return wrapper
    return _val_checker


@val_checker(check_arg)
def calc_cube(x):
    return x ** 3

if __name__=='__main__':
    print(calc_cube(2))