import time

now  = time.localtime()



for prop in now:
    print(prop);


print(now);


def print_time(t):
    year = t.tm_year
    month = t.tm_mon
    day = t.tm_mday
    print(year , ".", month , ".", day, sep="")


print_time(now)


now = time.gmtime()
print(now)


from datetime import time
from datetime import datetime
from datetime import date

now = datetime.now()
d = now.date()
t = now.time()

print(d)
print(t)


def print_d(d):
    year = d.year
    month = d.month
    day = d.day
    print(year, month , day)

def print_t(t):
    hour = t.hour
    min = t.minute
    sec = t.second
    print(hour , min , sec)


print_d(d)
print_t(t)



pattern = "%Y-%M-%d time: %h:%m:%s"
print(time.now().strftime(pattern))

