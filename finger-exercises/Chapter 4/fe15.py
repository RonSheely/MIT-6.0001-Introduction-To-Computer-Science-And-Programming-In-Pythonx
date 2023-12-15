"""Finger exercise: Write a function mult that accepts either one or
two ints as arguments. If called with two arguments, the function
prints the product of the two arguments. If called with one argument,
it prints that argument."""


def mult(number1: int = 1, number2: int = 1):
    print(number1 * number2)


mult()
