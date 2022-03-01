import datetime
# Write a Python program to subtract five days from current date.
# today = datetime.datetime.now()
today = datetime.date.today()
days = datetime.timedelta(5)
ans = today - days
print('Before 5 days from today: ',ans)

print('-'*70)
# Write a Python program to print yesterday, today, tomorrow.
print('Today: ',today)
yesterday = today - datetime.timedelta(1)
print('Yesterday: ',yesterday)
tomorrow = today + datetime.timedelta(1)
print('Tomorrow: ',tomorrow)

print('-'*70)
# Write a Python program to drop microseconds from datetime.
print('Datetime without microsecond',datetime.datetime.today().replace(microsecond=0))

print('-'*70)
# Write a Python program to calculate two date difference in seconds.
day1 = datetime.datetime.now()
day2 = day1 + datetime.timedelta(1)
print((day2 - day1).total_seconds())