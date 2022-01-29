# 모듈의 종류
#   1. 파이썬이 제공해주는 모듈(표준모듈)
#   2. 개발자가 직접만든 모듈
#   3. 제 3자가 제공하는 모듈

# import 모듈 [as alias] 
# from 모듈 import 함수명

# import math
# print(math.sqrt(2))

# from math import sqrt
# print(sqrt(2))

# import math as m 
# print(m.sqrt(2))

# from math import sqrt as sq
# print(sq(2))

# IoT에서는 time을 많이쓴다.
import time
print(time.time())      # 1970 / 1 / 1일로부터 ~ 만큼 지났다.
now = time.time()/60/60/24/365
print(now+1970)
print(time.ctime(time.time()))

print(time.localtime(time.time()))

print(time.localtime())     # 매개변수 안주면 자동으로 현재 시간을 측정하라라는 뜻
now1 = time.localtime()
print("%d년 %d월 %d일"%(now.tm_year, now.tm_mon, now.tm_mday))
print("%d:%d:%d" %(now.tm_hour, now.tm_min, now.tm_sec))


import datetime
now2 = datetime.datetime.now()
print("%d년 %d월 %d일" % (now.year, now.month, now.day))
print("%d:%d:%d" % (now.hour, now.minute, now.second))
