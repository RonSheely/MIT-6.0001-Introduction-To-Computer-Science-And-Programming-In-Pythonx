"""Finger exercise: Implement a function that satisfies the
specification"""

list_samp = [1, 1, 3, 5, 19]


def find_an_even(L):
    """Assumes L is a list of integers
    Returns the first even number in L
    Raises ValueError if L does not contain an even
    number"""
    for num in L:
        if num % 2 == 0:
            return num
    raise ValueError("No even number found in list")


find_an_even(list_samp)
