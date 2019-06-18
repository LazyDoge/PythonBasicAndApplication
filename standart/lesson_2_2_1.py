import datetime

year, month, day = input().split()

delta = int(input())

date = datetime.date(int(year), int(month), int(day))

dateResult = date + datetime.timedelta(delta)

# print(dateResult.strftime("%Y") + " " + str(dateResult.month) + " " + str(dateResult.day))
# print(dateResult.strftime("%Y %-m %-d"))
print(dateResult.strftime("%Y %#m %#d"))


# put your python code here
# import datetime
# https://shultais.education/blog/python-f-strings﻿
inp = datetime.datetime.strptime(input(), "%Y %m %d")
inp += datetime.timedelta(days=int(input()))
print(f'{inp.year} {inp.month} {inp.day}')

#
#

y, m, d = map(int, input().split())
days = int(input())

current = datetime.date(year=y, month=m, day=d)
current += datetime.timedelta(days=days)

print("{} {} {}".format(current.year, current.month, current.day))