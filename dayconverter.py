print('enter the number of days')
days = int(input())

years = days //365
weeks = (days % 365)//7
days_rem = days-years*365 - weeks*7
print('years:',years)
print('weeks',weeks)
print('Days remaining',days_rem)