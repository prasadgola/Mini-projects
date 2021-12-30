import datetime
intmonth,intday,intyear = raw_input().split()
month = int(intmonth)
day=int(intday)
year=int(intyear)
ans = datetime.date(year, month, day)
low = ans.strftime("%A")
print low.upper()08