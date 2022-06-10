# Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп
# (например «5 руб 04 коп»). Подумать, как из цены получить рубли и копейки, как добавить нули, если, например,
# получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).
# Вывести цены, отсортированные по возрастанию,
# новый список не создавать (доказать, что объект списка после сортировки остался тот же).
# Создать новый список, содержащий те же цены, но отсортированные по убыванию.
# Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?
#

price_list = [5.8, 46.51, 97, 56.08, 36.51, 99, 77.8, 43.31, 6, 155.2, 16.51]

i = 0
new_price = []
while i < len(price_list):
    len_price = len(str(price_list[i]))

    if len_price == 3:
        len_price = len(str(price_list[i]).split(".", 1))
        rub, cop = str(price_list[i]).split(".", 1)
        new_price.append(f'0{rub} руб 0{cop} коп')
    elif len_price == 4:
        len_price = len(str(price_list[i]).split(".", 1))
        rub, cop = str(price_list[i]).split(".", 1)
        new_price.append(f'{rub} руб 0{cop} коп')
    elif len_price > 4:
        len_price = len(str(price_list[i]).split(".", 1))
        rub, cop = str(price_list[i]).split(".", 1)
        new_price.append(f'{rub} руб {cop} коп')
    elif len_price == 2:
        rub = str(price_list[i])
        cop = '00'
        new_price.append(f'{rub} руб {cop} коп')
    elif len_price < 2:
        rub = '0' + str(price_list[i])
        cop = '00'
        new_price.append(f'{rub} руб {cop} коп')
    else:
        new_price.append(f'{rub} руб {cop} коп')
    i += 1


print(new_price)
print(id(new_price))
new_price.sort()
print(new_price)
print(id(new_price))
new_price.sort(reverse=True)

desc_price_list = new_price[0:5]
desc_price_list.sort()
print(new_price[0:5])