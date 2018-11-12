import calendar;
import time;


# for a in range(20,9):
#     print (a)
# for a in 'icta':
#     print(a)

# for a in range(20,9,-1):
#     print(a)
# list=[100,45,78,52,55,6,66,0]
# for x in list:
#     if x%2==0:
#         print(x)

mytime= time.localtime(time.time())

cal=calendar.month(2018,11);
print (mytime)
print(cal)