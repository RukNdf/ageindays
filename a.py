
age_in_days = int(input("What's you age in days?"))
year = int(age_in_days/365)
rem = age_in_days-(year*365)
month = int(rem/30)
rem -= (month*30)
day = int(rem/1)
print('Year {} month {} day {}'.format(year,month,day))