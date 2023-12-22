from time import time

current_number_of_seconds = time()

start_year = 1970
start_date = 1
start_month = 1

years = current_number_of_seconds // (365 * 24 * 60 * 60)
# print(days)
print(current_number_of_seconds)

from datetime import datetime

weekday_today = datetime.now().weekday()
weekday_tomorrow = datetime(2023, 12, 14).weekday()
weekday_monday = datetime(2023, 12, 11).weekday()
print("Today is", weekday_today)
print("Tomorrow is", weekday_tomorrow)
print("Monday was", weekday_monday)
