import re #

def email_parse(email: str) -> dict:
    """
    Парсит переданную email-строку на атрибуты и возвращает словарь
    :param email: строковое входное значение обрабатываемого email
    :return: {'username': <значение до символа @>, 'domain': <значение за символом @>} | ValueError
    """
    RE_MAIL = re.compile(r'^(([\w\d][\w\d.]+[\w\d])@([\w]+\.){1,2}[\w]{2,})$') # компилируем строковое регулярное выражение для email в переменную
    if RE_MAIL.match(email): # если адрес соответствует регулярному выражению почтового адреса,
        lst = email.split('@') # то разделяем его на логин и домен
        mail_dict = {'username': lst[0], 'domain': lst[1]}
        return mail_dict
    else:
        raise ValueError(f'wrong email {email}')


if __name__ == '__main__':
       email_parse('SergeyK87@geekbrains.ru')
       print(email_parse('SergeyK87@geekbrains.ru'))