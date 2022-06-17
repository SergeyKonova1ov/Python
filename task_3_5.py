
# 5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого):
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#         Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]

import random


def get_jokes(num: int = 2, flag: bool = True):
    """Returns random jokes
    num - number of jokes
    flag == True - only unique words
    flag == False - words can be repeated
    """
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    lst_jok = []
    lim = min(len(nouns), len(adverbs), len(adjectives))  # Определяем возможное кол-во уникальных слов
    if flag:
        if num <= lim:
            lst_a = []
            lst_b = []
            lst_c = []
            for n in range(num):
                a = random.randint(0, len(nouns) - 1)  # Создаем переменные с случайным индексом для каждого списка слов
                b = random.randint(0, len(adverbs) - 1)
                c = random.randint(0, len(adjectives) - 1)
                while a in lst_a or b in lst_b or c in lst_c:  # Проверяем, чтобы индексы в переменных не повторялись
                    a = random.randint(0, len(nouns) - 1)
                    b = random.randint(0, len(adverbs) - 1)
                    c = random.randint(0, len(adjectives) - 1)
                lst_a.append(a)  # Храним список уже использованных индексов
                lst_b.append(b)
                lst_c.append(c)
                lst_jok.append(' '.join([nouns[a], adverbs[b], adjectives[c]]))  # Шутка из слов со случайным индеком
            return lst_jok
        else:  # Предупреждение на случай, если запрашиваемое кол-во шуток больше, чем уникальных слов
            return f'Максимальное кол-во уникальных шуток - {lim}, введено {num}'
    elif not flag:  # Если flag == 0, то можем использовать любые случайные индексы в диапазоне списка слов
        for n in range(num):
            a = random.randint(0, len(nouns) - 1)
            b = random.randint(0, len(adverbs) - 1)
            c = random.randint(0, len(adjectives) - 1)
            lst_jok.append(' '.join([nouns[a], adverbs[b], adjectives[c]]))
        return lst_jok

print(get_jokes(5, 1))