import sys  # импортируем модуль, позволяющий передавать аргумент функции прямо из командной строки


def add(argv):
    pr, summ = argv  # argv- список аргументов, переданных из командной строки. pr - выполняемый модуль, summ - аргумент
    with open(file_name, 'a', encoding='utf-8') as fw:
        fw.write(str(summ) + '\n') # записать введенную сумму с переносом строки


file_name = 'bakery.csv'

if __name__ == '__main__':
    sys.exit(add(sys.argv))  # используем функцию для передачи аргумента из командной строки
