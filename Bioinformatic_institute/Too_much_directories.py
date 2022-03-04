from pathlib import Path
import glob

a = set()
package = sorted(glob.glob('C:/Users/Hurricane/PycharmProjects/main/**/*.py', recursive=True))
for name in package:
    a.add(name[name.index('main'):-9])

j = sorted(list(a))

with open('C:/Users/Hurricane/Downloads/database.txt', 'w', encoding='UTF-8') as of:
    for i in j:
        print(i, file=of)
    print(*j, sep='\n')


# j = os.walk('C:/Users/Hurricane/PycharmProjects/main', topdown=True, onerror=None, followlinks=False)
#
# cs = set()
#
# for a, b, c in j:
#     for i in c:
#         if '.py' in i:
#             print(a[a.index('main'):])
#             cs.add(a[a.index('main'):])
#
# print(cs)