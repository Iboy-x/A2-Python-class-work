import datetime

thisDay = datetime.date.today()
print(thisDay)
nextDay = thisDay + datetime.timedelta(days=10, weeks= 10)
print(nextDay)