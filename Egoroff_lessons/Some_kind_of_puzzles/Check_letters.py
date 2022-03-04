import re
def count_letters(s):
    N = len(re.findall("[А-ЯA-Z]", s))
    K = len(re.findall("[а-яa-z]", s))
    print(f'Количество заглавных символов: {N}\nКоличество строчных символов: {K}')


count_letters('Привет, Старина  ')