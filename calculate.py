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