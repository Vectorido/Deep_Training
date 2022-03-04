import time, datetime
a = time.strptime('12:40', '%H:%M')
s = datetime.timedelta(hours=a.tm_hour, minutes=a.tm_min, seconds=a.tm_sec).seconds
print(s)
