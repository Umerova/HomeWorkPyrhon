import datetime
timestamp = int(input())
dt = datetime.datetime.fromtimestamp(timestamp)
years = int((timestamp / (365 * 24 * 60 * 60)) + 1970)
print(years)
