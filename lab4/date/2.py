# Write a Python program to print yesterday, today, tomorrow.
import datetime

tday = datetime.date.today()

deltaday = datetime.timedelta(days=1)
print("Yesterday: ", tday - deltaday)
print("Today: ", tday)
print("Tomorrow: ", tday + deltaday)