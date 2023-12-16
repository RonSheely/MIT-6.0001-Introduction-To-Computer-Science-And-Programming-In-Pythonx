"""Finger exercise: Using the algorithm of Figure 3-6, write a
function that satisfies the specification"""


def log(x, base: int, epsilon):
    """Assumes x and epsilon int or float, base an int,
    x > 1, epsilon > 0 & power >= 1
    Returns float y such that base**y is within epsilon
    of x."""
    if x < 1:
        raise ValueError("X must be greater than 1")
    if epsilon < 0:
        raise ValueError("Epsilon must be greater than 0")
    if not base > 1:
        raise ValueError("Base value must be greater than 1")
    low = 0
    high = x / base
    ans = (high + low) / 2
    while abs(base**ans - x) >= epsilon:
        if base**ans < x:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2
    return ans


print(log(1234, 2, 0.001))
