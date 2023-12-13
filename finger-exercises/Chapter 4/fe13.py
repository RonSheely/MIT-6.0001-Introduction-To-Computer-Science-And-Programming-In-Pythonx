"""Finger exercise: Write a function is_in that accepts two strings as
arguments and returns True if either string occurs anywhere in the
other, and False otherwise. Hint: you might want to use the built-in
str operator in"""


def is_in(string_a, string_b):
    return string_a in string_b


return_value = is_in("12", "Yes123123")
print(return_value)
