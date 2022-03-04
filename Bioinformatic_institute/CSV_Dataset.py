# Поиск необходимого значения в CSV-файле при помощи библиотеки pandas

import pandas as pd

crimes = pd.read_csv('C:/Users/Hurricane/Downloads/Crimes.csv')
required_year = crimes.loc[crimes['Date'].str.contains('2015')]

print(required_year['Primary Type'].value_counts().idxmax())


# CSV - вариант
# import csv
# with open('C:/Users/Hurricane/Downloads/Crimes.csv', 'r', encoding='UTF-8') as crimes:
#     reader = csv.reader(crimes, delimiter=',')
#     for i in reader:
#         if i[2][6:10] == '2015':
#             print(i)

# общее описание столбца, включая most frequent value
# print(required_year['Primary Type'].describe())

# с библиотекой datetime
# df[df.Date.datetime.year == 2015]['Primary Type'].value_counts().idxmax())

# возможность совершения стандартного запроса SQL
# pysqldf = lambda q: sqldf(q, globals())
# ton = sqldf("select * from df where Date like '%2015%';", locals())
# print(ton['Date'])
