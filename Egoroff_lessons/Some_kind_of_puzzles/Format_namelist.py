def format_namelist(k):
    a = []
    for i in k:
        a.append(i['name'])
    if len(a) == 1:
        return a[0]
    elif len(a) > 1:
        return ', '.join(a[:-1]) + ' и ' + a[-1]
    return ''

print(format_namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}, {'name': 'Homer'}, {'name': 'Marge'}]))