# Write a Python program to calculate two date difference in seconds.

import datetime

tdelta = datetime.timedelta(days=2)

print(tdelta.total_seconds())