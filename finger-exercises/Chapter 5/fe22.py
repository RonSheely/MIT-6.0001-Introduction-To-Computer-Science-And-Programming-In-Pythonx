"""Finger exercise: Implement a function that meets the specification"""


test_dictionary = {"x": 11, "b": 12}


def get_min(d):
    """d a dict mapping letters to ints
    returns the value in d with the key that occurs first
    in the alphabet. E.g., if d = {x = 11, b = 12}, get_min
    returns 12."""
    return d[min(d)]


print(get_min(test_dictionary))
