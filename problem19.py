# problem 19

def get_number_days(month, year):
    if month == 'February':
        if year % 100 == 0 and year % 400 == 0:
            return 29
        elif year % 100 == 0 and year % 400 != 0:
            return 28
        elif year % 100 != 0 and year % 4 == 0:
            return 29
        else:
            return 28
    if month in {'January', 'March', 'May', 'July', 'August', 'October', 'December'}:
        return 31
    elif month in {'September', 'April', 'June', 'November'}:
        return 30
    else:
        return 'ERROR'

months = ['January', 'February', 'March', 'April',
          'May', 'June', 'July', 'August',
          'September', 'October', 'November', 'December']
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday', 'Saturday']
current_year = 1900
current_month = 0
current_day_week = 1

count_days = 0

while current_year != 2001:
    if current_day_week == 0 and current_year > 1900:
        count_days += 1
    current_day_week += get_number_days(months[current_month], current_year)
    current_day_week %= 7
    current_month += 1
    current_month %= 12
    if current_month == 0:
        current_year += 1

print count_days
