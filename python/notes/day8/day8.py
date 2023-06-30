from datetime import date,time,datetime
import pytz

#time stuff

#Example 3
local = datetime.now()
print("Local: ",local.strftime("%m/%d/%Y, %H:%M:%S"))

tz_NY = pytz.timezone('America/New_York')
datetime_NY = datetime.now(tz_NY)

print("NC: ", datetime_NY.strftime("%m/%d/%Y, %H:%M:%S"))

tz_Ch = pytz.timezone('America/Chicago')
datetime_Ch = datetime.now(tz_Ch)

print("MN: ", datetime_Ch.strftime("%m/%d/%Y, %H:%M:%S"))

tz_London = pytz.timezone('Europe/London')
datetime_London = datetime.now(tz_London)

print("London: ", datetime_London.strftime("%m/%d/%Y, %H:%M:%S"))

input()#prevent running old code notes
#Example 2
f = date(2018,7,12)
g = date(year=2017, month=6, day=4)
h = f - g
print("date compared: ", h)

i = datetime(2018,6,19,10,15,23)
j = datetime(year=2020,month=2,day=1,hour=9,minute=55,second=9)
k= i - j
print('datetime compared',k)

print(h - k)

#Example 1
a = time()
b = time(11, 23, 45)
c = time(hour=12,minute=23,second=12)
d = time(9, 43, 5, 334556)
e = datetime(2023,6,29,10,4,55,2345)
print(a,b,c,d,e)
print(d.microsecond)

# date stuff
timestamp =date.fromtimestamp(123561341)

todays_date = date.today()

print("Today's year = ", todays_date.year)
print("Today's month = ", todays_date.month)
print("Today's day = ", todays_date.day)

print("Date =", timestamp)