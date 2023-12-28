"""Finger exercise: Write a list comprehension that generates all
non-primes between 2 and 100."""


y = [x for x in range(4, 100) if any(x % y == 0 for y in range(2, int(x**0.5) + 1))]

print(y)
