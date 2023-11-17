"""Finger exercise: Write code that asks the user to enter their
birthday in the form mm/dd/yyyy, and then prints a string of the
form ‘You were born in the year yyyy.’"""


user_date = input("What is your date of birth? (MM/DD/YYYY): ")
if len(user_date) > 10:
    raise ValueError("Input Too Long")
print(f"You were born in the year {user_date[6:]}")
