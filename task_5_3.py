"""Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>), например:
('Иван', '9А')
('Анастасия', '7В')
Количество генерируемых кортежей не должно быть больше длины списка tutors. Если в списке klasses меньше элементов,
чем в списке tutors, необходимо вывести последние кортежи в виде: (<tutor>, None)
"""

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б']


def check_gen(tut: list, kl: list): # создаем генератор
    for i in range(len(tutors)):
        try:
            yield tut[i], kl[i] # пытаемся соединить индексы двух списков
        except IndexError: # если получаем ошибку индекса, то возращаем none
            yield tut[i], None


generator = check_gen(tutors, klasses) # используем с нашими списками tutors  klasses
print(type(generator))
for i in range(len(tutors)):
    print(next(generator))