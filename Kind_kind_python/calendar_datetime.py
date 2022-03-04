from datetime import datetime, timedelta
a, b = 2, 28
dt = datetime.strptime(f'{a}/{b}', "%m/%d")

next_day = dt + timedelta(days=1)
previous_day = dt - timedelta(days=1)

a = next_day.strftime("%m.%d")
b = previous_day.strftime("%m.%d")

print(a, b)