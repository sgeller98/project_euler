# Project Euler Problem 19

import datetime

start = datetime.date(1901, 1, 1)  # 1901 Jan 1
end = datetime.date(2000, 12, 31)  # 2000 Dec 31

totalSundays = 0
for day in range(1, (end - start).days+1):
    day = datetime.timedelta(days=day)
    if (start + day).weekday() == 6 and (start + day).day == 1:
        totalSundays += 1

print(totalSundays)
