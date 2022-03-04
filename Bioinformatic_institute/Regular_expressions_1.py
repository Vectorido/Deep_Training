import re

#                   --- Метасимволы ---
# [] ~ содержит отдельные символы и диапазоны значений ([abc] = a, b или с)
# - ~ диапазон ([a-d])
# ^ ~ определяет начало строки (^[Mm] в начале должна стоять либо буква M либо m
# . ~ любой символ (a.c = abc, aRc, a+c и т.д.)
# * ~ символ должен быть в этой строке ноль или несколько раз (ab*c = ac, abbc, abbbbc, но не bbc)
# + ~ символ должен быть в этой строке хотя бы один раз (ab+c = abc, abbbbbc, но не ac)
# ? ~ символ должен быть в этой строке ноль или один раз(ab?c = ac, abc)
# {} ~ количество вхождений символа (ab{3, 5}c = abbbc, abbbbc, abbbbbc)
# () ~ содержит группу значений ((abs) = creabs, absolute, но не abas)
# ^ ~ отрицание вхождения
# | ~ ИЛИ
# \d ~ [0-9] цифры
# \D ~ [^0-9] не цифры
# \s ~ [ \t\n\r\f\v] пробельные символы
# \S ~ [^ \t\n\r\f\v] не пробельные символы
# \w - [a-ZA-Z0-9_] буквы + цифры + '_'
# \W - [^a-ZA-Z0-9_] не буквы, не цифры, не '_'
# \. - в конце должна быть точка
# \  ~ само по себе разделение либо специальное выражение

pattern = r"a[a-zA-Z]c"
string = 'acc'
match_object = re.match(pattern, string)
search_object = re.search(pattern, string)

string = 'abc, acc, aac'
all_inc = re.findall(pattern, string)
print(all_inc)

a = r"a[ab]+a"
a_2 = r"a[ab]+?a"
b = 'abaaba'
print(re.findall(a, b)) # выбирает строку максимальной длины из подходящих, жадный способ
print(re.findall(a_2, b)) # нежадный способ


# fixed_typos = re.sub(pattern, 'abc', string)
# print(fixed_typos)

#print(match_object, search_object, sep='\n')