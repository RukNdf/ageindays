def calcD(age_in_days):
    year = int(age_in_days/365)
    rem = age_in_days-(year*365)
    month = int(rem/30)
    rem -= (month*30)
    day = int(rem/1)
    return (year,month,day)
    
def printF(date):
    year, month, day = date
    print(str(year) + ' ano(s)')
    print(str(month) + ' mes(es)')
    print(str(day) + ' dia(s)')
    
    
        
if __name__ == '__main__':
    age_in_days = int(input(""))
    printF(calcD(age_in_days))
