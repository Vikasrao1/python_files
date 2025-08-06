# date time module - help deal with timestamps in the code
import datetime
t = datetime.time(5, 30, 1)
# to see the diff components
print(t)
print('hour :' , t.hour)
print('minute:' , t.minute)
print('second:', t.second)
print('microsecond:', t.microsecond)
print('tzinfo:', t.tzinfo)

# to chekc min & max values of time
print('Earliest:', datetime.time.min)
print('Latest:', datetime.time.max)
print('Resolution:',datetime.time.resolution)

# Dates

today = datetime.date.today()
print(today)
print('ctime:', today.ctime())
print('Year:', today.year)
print('Month:', today.month)
print('Day:', today. day)

# Another way to create new date instance, uses replace() method
d1 = datetime.date(2022, 2, 27)
print('d1:',d1)
d2 = d1.replace(year=2010)
print('d2:', d2)