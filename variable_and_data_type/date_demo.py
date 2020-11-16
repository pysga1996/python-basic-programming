import datetime as dt

x = dt.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A"))

y = dt.datetime(2020, 5, 17)
print(y)
# Weekday, short version
print(y.strftime("%a"))
# Weekday, full version
print(y.strftime("%A"))
# Weekday as a number 0-6, 0 is Sunday
print(y.strftime("%w"))
# Day of month 01-31
print(y.strftime("%d"))
# Month name, short version
print(y.strftime("%b"))
# Month name, full version
print(y.strftime("%B"))
# Month as a number 01-12
print(y.strftime("%m"))
# Year, short version, without century
print(y.strftime("%y"))
# Year, full version
print(y.strftime("%Y"))
# Hour 00-23
print(y.strftime("%H"))
# Hour 00-12
print(y.strftime("%I"))
# AM/PM
print(y.strftime("%p"))
# Minute 00-59
print(y.strftime("%M"))
# Second 00-59
print(y.strftime("%S"))
# Microsecond 000000-999999
print(y.strftime("%f"))
# UTC offset
print(y.strftime("%z"))
# Timezone
print(y.strftime("%Z"))
# Day number of year 001-366
print(y.strftime("%j"))
# Week number of year, Sunday as the first day of week, 00-53
print(y.strftime("%U"))
# Week number of year, Monday as the first day of week, 00-53
print(y.strftime("%W"))
# Local version of date and time
print(y.strftime("%c"))
# Local version of date
print(y.strftime("%x"))
# Local version of time
print(y.strftime("%X"))
# A % character
print(y.strftime("%%"))
