def calcD(age_in_days):
    year = int(age_in_days/365)
    rem = age_in_days-(year*365)
    month = int(rem/30)
    rem -= (month*30)
    day = int(rem/1)
    return (year,month,day)
        
age_in_days = int(input(""))
year, month, day = calcD(age_in_days)
print(str(year) + ' ano(s)')
print(str(month) + ' mes(es)')
print(str(day) + ' dia(s)')
