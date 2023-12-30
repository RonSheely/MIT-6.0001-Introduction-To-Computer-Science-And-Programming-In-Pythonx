"""Finger exercise: Since 1958, Canadian Thanksgiving has occurred
on the second Monday in October. Write a function that takes a year
(>1957) as a parameter, and returns the number of days between
Canadian Thanksgiving and Christmas."""
import calendar as cal

CHRISTMAS_DATE = 25


def find_thanksgiving(year):
    assert year > 1957, "Given year must be greater than, 1957"
    month = cal.monthcalendar(year, 10)
    if month[0][cal.MONDAY] != 0:
        thanksgiving = month[1][cal.MONDAY]
    else:
        thanksgiving = month[2][cal.MONDAY]
    return thanksgiving


def shopping_days(year: int):
    assert year > 1957, "Given year must be greater than, 1957"
    october = cal.monthcalendar(year, 10)
    november = cal.monthcalendar(year, 11)
    thanksgiving_date = find_thanksgiving(year)
    max_days_october = max(max(october))
    max_days_november = max(max(november))
    return (max_days_october - thanksgiving_date) + max_days_november + CHRISTMAS_DATE


x = shopping_days(2023)
print(x)
