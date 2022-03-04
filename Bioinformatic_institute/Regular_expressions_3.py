import re

#x = re.match(r'text', "TEXT", re.IGNORECASE | re.DEBUG) # игнорирует регистр и показывает информацию в режиме дебага
#print(x)

#print(re.__doc__)
#
# f = ['cat and cat', 'cat', 'catcat', 'casottca']
#
# for i in f:
#     if re.search(r'cat.*cat', i):
#         print(i)


f = [input() for i in range(5)]


for i in f:
    if re.search(r'\b(\w+)\b', i):
        print(i)
    print(re.findall(r'\b(\w+)\1\b', i))