"""Finger exercise: When the implementation of fib in Figure 6-3 is
used to compute fib(5), how many times does it compute the value
of fib(2) on the way to computing fib(5)?"""


def fib(x: int):
    if x == 2:
        print("Two Computed")
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x - 1) + fib(x - 2)


print(fib(5))
