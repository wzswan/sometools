#设a为字符串
import time
a = "2011-09-28 10:00:00"
 
#中间过程，一般都需要将字符串转化为时间数组
time.strptime(a,'%Y-%m-%d %H:%M:%S')
>>time.struct_time(tm_year=2011, tm_mon=9, tm_mday=27, tm_hour=10, tm_min=50, tm_sec=0, tm_wday=1, tm_yday=270, tm_isdst=-1)
 
#将"2011-09-28 10:00:00"转化为时间戳
time.mktime(time.strptime(a,'%Y-%m-%d %H:%M:%S'))
>>1317091800.0
 
#将时间戳转化为localtime
x = time.localtime(1317091800.0)
time.strftime('%Y-%m-%d %H:%M:%S',x)
 
#获取当前日期
time.strftime("%Y-%m-%d")
>>>'2015-03-13'
 
#获取当前时间
 
time.strftime("%Y-%m-%d %H:%M:%S")
>>>'2015-03-13 20:26:22'