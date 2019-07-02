##this is an example of time module
import time
import calendar
#print(time)
t=time.time()
print(t)
t1=time.localtime(time.time())
print(t1)
t=time.asctime(time.localtime(time.time()))
print(t)
print(time.ctime())
print(time.gmtime())
print(time.localtime())
print("start:"+time.ctime())
time.sleep(5.0)
print("end:"+time.ctime())
##print(time.strftime("%T %H %I %M %S %B %d %Y %j %m %u %U",time.localtime(time.time())))
##print("current time:hour:minute:second:current date:day of year:month no.:week day:week no. of year:")
##print(calendar.calendar(2016,w=3,l=2,c=5))
##c=calendar.isleap(2016)
##print(c)
##print(calendar.month(2016,8,w=2,l=2))
##print(calendar.monthcalendar(2016,8))
##print(calendar.weekday(2016,8,14))
t=time.strftime("%Y-%m-%d",time.localtime(time.time()))
print("date:"+t)


c=calendar.month(2016,8)

print(c)
