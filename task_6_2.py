def find_spamer(filename):
    ip_list = [] # список айпи адресов
    with open(filename, 'r', encoding='utf-8') as fr:  # Открываем файл на чтение в кодировке utf-8

        for line in fr:  # в каждой строке нашего файла
            res = line.split(' ')[0] # разделяем строку по пробелу и вытаскиваем 0й элемент, который является айпи адресом
            ip_list.append(res)  # все полученные ip вставляем в список

    counter = {}  # Создаем словарь со счетчик айпи адресов

    for ip in ip_list:  # подсчитываем количество ip в нашем списке: проверяем, есть ли ip в словаре, если нет, добавляем новое значение ключа +1 (счетчик)
        if ip in counter:
            counter[ip] += 1
        else:
            counter[ip] = 1

    counter_sorted = sorted(counter.items(), key=lambda i: i[1], reverse=True)  # Получившийся список сортируем по значению ключа и по убыванию.

    return counter_sorted[0][0], counter_sorted[0][1]  # Возвращаем из этого списка первый кортеж с  ip и кол-во запросов. Это и будет спамер


file = 'nginx_logs.txt' # имя файла
sp_ip, count = find_spamer(file) # помещаем результат выполнения функции в переменную
print(f'ip: {sp_ip}, count: {count}')