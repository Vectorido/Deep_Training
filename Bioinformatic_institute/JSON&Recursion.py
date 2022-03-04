import json

initial = json.loads("""[
  {"name": "kvrwxkmqfy", "parents": ["zemrehxvuo", "qzntzflodp", "pjvisgmdrw"]},
  {"name": "ogqoyccgkn", "parents": ["ppcmlxqgmn", "titthqeskb"]},
  {"name": "uhfdrfrhzx", "parents": ["ogqoyccgkn", "ppcmlxqgmn", "wubwjzolrx", "pjvisgmdrw", "titthqeskb"]},
  {"name": "zemrehxvuo", "parents": ["uhfdrfrhzx", "wubwjzolrx", "pjvisgmdrw", "titthqeskb"]},
  {"name": "ppcmlxqgmn", "parents": ["pjvisgmdrw", "thceozowkb"]},
  {"name": "qzntzflodp", "parents": ["wubwjzolrx", "titthqeskb", "thceozowkb"]},
  {"name": "wubwjzolrx", "parents": []},
  {"name": "pjvisgmdrw", "parents": []},
  {"name": "titthqeskb", "parents": ["wubwjzolrx", "pjvisgmdrw"]},
  {"name": "thceozowkb", "parents": ["pjvisgmdrw", "titthqeskb"]}
]""")

with_children = {element['name']: [] for element in initial}

for el_i in initial:
    for elc in with_children:
        if elc in el_i['parents']:
            with_children[elc].append(el_i['name'])

for element in with_children:
    with_children[element] = set(with_children[element])


def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited


for element in sorted(with_children.keys()):
    print(element, ':', len(dfs(with_children, element)))
    # print(r)

# print(graph_2)

# Required OUTPUT

# Aaa : 1
# Bb : 2
# C : 2
# D : 9
# E : 4
# Ff : 5
# G : 8
# I : 3
# Y : 9
# Zz : 7
