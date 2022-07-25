import requests

from datetime import datetime as dt


def currency_rates_adv(char_code: str):
    """ Вывод курса валюты и даты сервера"""

    char_code = char_code.upper()  # Преводим вводные данные к верхнему регистру
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    res = requests.get(url)  # GET запрос к сайту
    res_date = res.headers['Date']  # Получаем дату с сервера
    txt = res.text  # Отражаем полученные данные ввиде текста
    start_inx = txt.find(char_code)  # Ищем код запрашиваемой валюты в тескте. Если не найдем, вернет -1

    if start_inx != -1:
        val_inx = txt.find('<Value>', start_inx) + 7  # Начальный индекс курса валюты
        val = txt[val_inx:val_inx + 7]
        fulldate = dt.strptime(res_date, '%a, %d %b %Y %H:%M:%S %Z')  # Приводим значение даты к типу date
        dat = fulldate.date()

        return val, dat
