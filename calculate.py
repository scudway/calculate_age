daysOfMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap_year(year):
    if year % 4 != 0:
        return False
    elif year % 400 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


def days_in_months(y,m,d):
    # find the number of days in the number of months
    # add pre-defined number of days passed in d variable
    days = d
    for i, j in enumerate(daysOfMonths):
        # we must stop at a month before -> m-1 , because we already have days in d
        if i < m-1:
            days += j

    # add 29th february if its a leap year
    if is_leap_year(y) and m > 2:
        days += 1

    return days


def days_in_year(y):
    # find the number of days in a giver year. leap year = 366 , non leap year = 365
    if is_leap_year(y):
        return 366
    else:
        return 365