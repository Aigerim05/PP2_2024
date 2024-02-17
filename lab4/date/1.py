# Write a Python program to subtract five days from current date.
import datetime

tday = datetime.date.today()
tdelta = datetime.timedelta(days=5)
print(tday - tdelta)