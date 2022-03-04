# Парсер для нахождения доменов вместе с именами поддоменов в тексте на URL-странице и сортировки их по алфавиту.
# Наиболее сложное задание по регулярным выражениям. Естественно, парсить вне обучения через регулярки бессмысленно.

import re
import requests
from urllib.parse import urlparse

a = 'https://pastebin.com/raw/7543p0ns'  # test_site

list_of_sites = re.findall(r'(<a.+href=[^ .]+?)([\w_-]+((?:\.[\w_-]+)+))([\w.-]*[\w-])*', requests.get(a).text)

s = [i[1] for i in list_of_sites]

print(*sorted(list(set(s))), sep='\n')
print(len(set(s)))
