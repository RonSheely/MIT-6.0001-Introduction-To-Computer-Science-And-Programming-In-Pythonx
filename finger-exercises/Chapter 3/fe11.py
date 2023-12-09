"""Finger exercise: Add some code to the implementation of
Newton–Raphson that keeps track of the number of iterations used
to find the root. Use that code as part of a program that compares the
efficiency of Newton–Raphson and bisection search. (You should
discover that Newton–Raphson is far more efficient.)"""


steps = 0
k = 24
epsilon = 0.01
guess = k/2
while abs(guess**2 - k) >= epsilon:
    steps += 1
    guess = guess - (((guess**2) - k)/(2*guess))
print("Square root of", k, "is about", guess, "found in", steps, "steps")
