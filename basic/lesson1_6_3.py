import time


class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))


class LoggableList(Loggable, list):
    def append(self, appendable):
        list.append(self, appendable)
        Loggable.log(self, appendable)


vara = LoggableList()
vara.append("xnj")
print(vara)