"""Finger exercise: Write an expression that evaluates to the mean of
a tuple of numbers. Use the function sum."""


def find_mean(tup: tuple):
    return sum(tup) / len(tup)


print(find_mean((1, 2, 3, 4,)))
