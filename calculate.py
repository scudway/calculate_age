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


def days_between_dates(y1, m1, d1, y2, m2, d2):
    # calculating the total number of days
    total_days = 0
    current_year = y1
    while current_year < y2:
        total_days += days_in_year(current_year)
        current_year += 1

    # we calculated the number of days between y1 to y2, we take off the number of days after y1, and we add the number
    # of days after y2.
    total_days = total_days - days_in_months(y1,m1,d1) + days_in_months(y2,m2,d2)
    return total_days