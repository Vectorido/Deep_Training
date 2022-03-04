import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))


class LoggableList(list, Loggable):

    def append(self, msg):
        x = super(LoggableList, self).append(msg)
        super().log(msg)

a = LoggableList()
a.append(14)
a.append(133)
a.append(2214)
print(a)