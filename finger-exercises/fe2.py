user_date = input("What is your date of birth? (MM/DD/YYYY): ")
if len(user_date) > 10:
    raise ValueError("Input Too Long")
print(f"You were born in the year {user_date[6:]}")
