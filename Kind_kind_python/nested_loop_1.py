import sys

# считывание списка из входного потока
lst_in = [
    'django chto  eto takoe    poryadok ustanovki',
    'model mtv   marshrutizaciya funkcii  predstavleniya',
    'marshrutizaciya  obrabotka isklyucheniy       zaprosov perenapravleniya'
]

lst_out =[]

for i in lst_in:
    while '  ' in i:
        i = i.replace('  ', ' ')
    i = i.replace(' ', '-')
    lst_out.append(i)


for i in lst_out:
    print(i)
