
# Сформировать и вывести на экран фразы вида: 'Привет, Игорь!' Подумать, как получить имена сотрудников из
# элементов списка, как привести их к корректному виду."

list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

i = 0
while i < len(list):
    # Разделяем элемент по пробелам. Берем последнюю посдтроку (имя).
    # Применяем нижний регистр, первая буква заглавная.
    name = list[i].split(' ')[-1].lower().title()
    result = ("Привет, %s!" %name)
    print(result)
    i += 1

