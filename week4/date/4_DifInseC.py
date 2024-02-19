
from datetime import datetime, time

def date_diff_in_Seconds(dt2, dt1):
  timedelta = dt2 - dt1
  return timedelta.days * 24 * 3600 + timedelta.seconds

date1 = datetime.strptime('2005-01-13 10:00:00', '%Y-%m-%d %H:%M:%S')

date2 = datetime.now()


print("\n%d seconds" %(date_diff_in_Seconds(date2, date1)))
print()