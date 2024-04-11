
from datetime import datetime

now = datetime.now()

def print_date(date):
    print('year:',date.year)
    print('month:',date.month)
    print('day:',date.day)
    print('hour:',date.hour)
    print('minute:',date.minute)
    print('seconds:',date.second)
    print('timestamp', date.timestamp())

print_date(now)

year_2023 = datetime(2023,1,1)

print_date(year_2023)



from datetime import time

current_time = time(21,6,10)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)


from datetime import date

current_date = date.today()

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(2024,6,13)

print(current_date.year)
print(current_date.month)
print(current_date.day)


# Operaciones con fechas

diff = year_2023 - now
print(diff)

from datetime import timedelta

start_time_delta = timedelta(200,100,100,weeks=10)
end_time_delta = timedelta(300,100,100,weeks=13)

print(end_time_delta - start_time_delta)
print(end_time_delta + start_time_delta)




