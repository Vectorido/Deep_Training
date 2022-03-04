import re

# pattern = r" english\?"
# string = 'Do you speak english?'
# match = re.search(pattern, string)
# print(match)

# pattern = r"((abc)|(test|text)*)"
# string = 'testtext'
# match = re.match(pattern, string)
# print(match)
# print(match.group(0))

pattern = r"((\w+)-\2)" # номер соответствует номеру группы (). Возвращает вторую группу
string = 'test-test chow-chow'
match = re.match(pattern, string)
duplicates = re.sub(pattern, r"\1", string) # поиск по первой группе
show_me_the_magic = re.findall(pattern, string) # список кортежей соответствий
print(match, duplicates, show_me_the_magic, sep='\n')
