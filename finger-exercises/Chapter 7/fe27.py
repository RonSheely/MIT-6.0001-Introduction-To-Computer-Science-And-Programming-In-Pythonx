"""Finger exercise: Write a function that meets the specification"""
import calendar as cal

CHRISTMAS_DATE = 25


def find_thanksgiving(year):
    month = cal.monthcalendar(year, 11)
    if month[0][cal.THURSDAY] != 0:
        thanksgiving = month[3][cal.THURSDAY]
    else:
        thanksgiving = month[4][cal.THURSDAY]
    return thanksgiving


def shopping_days(year: int):
    """year a number >= 1941 returns the number of
    days between U.S. Thanksgiving and Christmas in year"""
    assert year >= 1941, "Given year must be greater than, or equal to, 1941"
    november = cal.monthcalendar(year, 11)
    thanksgiving_date = find_thanksgiving(year)
    max_days_november = max(max(november))
    return (max_days_november - thanksgiving_date) + CHRISTMAS_DATE


x = shopping_days(2022)
print(x)
