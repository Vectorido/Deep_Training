def domain_name(url: str) -> str:
    url = url.replace('http://', '').replace('https://', '').replace('www.', '')
    return url.split('.')[0]

    pass

print(domain_name("www.xakep.ru"))