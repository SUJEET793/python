# import time
# ticks = time.time()
# print("The number of ticks since 12:00am, January 1, 1970:", ticks)
# ## here we can see that the time class calculate the no second
# #since 12:00am, January 1, 1970
#
# import time;
# localtime = time.localtime(time.time())
# print("Local current time :", localtime)
# #Local current time : time.struct_time(tm_year=2020,
# # tm_mon=4, tm_mday=23, tm_hour=18, tm_min=18, tm_sec=8, tm_wday=3,
# # tm_yday=114, tm_isdst=0)
#
# from datetime import date
# # here inside the datetime package there exist
# # date module which contain the
# # the following function
# td=date.today()
# print("Today is: ",td) # Today is:  2020-04-23
# day=td.day
# print("Day is: ",day) # Day is:  23
#
#
# print(td.month) # 4
# print(td.year) # 2020
# print(td.weekday()) #3
# print(date.weekday(td)) #3
#

# from datetime import datetime
# x=datetime.now()
# print(x.strftime("%y")) #20
# print(x.strftime("%Y")) # 2020
# print(x.strftime("%a")) # Thu  (weekday ,short version)
# print(x.strftime("%A")) # Thursday (weekday in the full viersion
# print(x.strftime("%b")) # Apr ( month in the short form )
# print(x.strftime("%B")) # April (month name i the full form)
# print(x.strftime("%A %d %B,%y")) # Thursday 23 April,20  (weekday ,day of the month ,month name,year)
# print(x.strftime("%A %D %B,%Y")) # Thursday 04/23/20 April,2020

import calendar
calendar.monthcalendar