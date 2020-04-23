import time
ticks = time.time()
print("The number of ticks since 12:00am, January 1, 1970:", ticks)
## here we can see that the time class calculate the no second
#since 12:00am, January 1, 1970

import time;
localtime = time.localtime(time.time())
print("Local current time :", localtime)
#Local current time : time.struct_time(tm_year=2020,
# tm_mon=4, tm_mday=23, tm_hour=18, tm_min=18, tm_sec=8, tm_wday=3,
# tm_yday=114, tm_isdst=0)

from datetime import date
# here inside the datetime package there exist
# date module which contain the
# the following function
td=date.today()
print("Today is: ",td) # Today is:  2020-04-23
day=td.day
print("Day is: ",day) # Day is:  23


print(td.month) # 4
print(td.year) # 2020
print(td.weekday()) #3
print(date.weekday(td)) #3

