####  Time_Delta


import datetime


from datetime import datetime


def time_delta(t1, t2):
  time_format = "%a %d %b %Y %H:%M:%S %z"
  time1 = datetime.strptime(t1, time_format)
  time2 = datetime.strptime(t2, time_format)
  return int(abs(time1 - time2).total_seconds())


for i in range(int(input())):
  t1 = input()
  t2 = input()
  print(time_delta(t1,t2))


# Test case:
# Input :
# 2
# Sun 10 May 2015 13:54:36 -0700
# Sun 10 May 2015 13:54:36 -0000
# Sat 02 May 2015 19:54:36 +0530
# Fri 01 May 2015 13:54:36 -0000

# output: 88200
