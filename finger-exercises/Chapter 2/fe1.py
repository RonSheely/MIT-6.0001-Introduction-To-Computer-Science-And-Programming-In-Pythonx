"""Finger exercise: Write a program that examines three variables—
x, y, and z—and prints the largest odd number among them. If none
of them are odd, it should print the smallest value of the three."""


def largest_odd_number(*args):
    divisible_by_3 = []
    for number in args:
        if number % 2 != 0:
            divisible_by_3.append(number)
    if not divisible_by_3:
        return_value = min(args)
    else:
        return_value = max(divisible_by_3)
    return return_value


x = largest_odd_number(2, 4, 6)
print(x)
