"""Finger exercise: What is the asymptotic complexity of each of the
following functions?"""


def g(L, e):
    """L a list of ints, e is an int"""
    for i in range(100):
        for e1 in L:
            if e1 == e:
                return True
    return False
    # O(n)


def h(L, e):
    """L a list of ints, e is an int"""
    for i in range(e):
        for e1 in L:
            if e1 == e:
                return True
    return False
    # O(L * e) or O(n**2)
