"""Finger exercise: Write a program that prints the sum of the prime
numbers greater than 2 and less than 1000. Hint: you probably want
to use a for loop that is a primality test nested inside a for loop that
iterates over the odd integers between 3 and 999."""


def check_for_prime(input_number: int) -> bool:
    for x in range(2, input_number - 1):
        if input_number % x == 0:
            return False
    return True


def add_primes() -> int:
    prime_sum = 0
    for x in range(1, 999, 2):
        # print(f"Number is {x}, prime?: {check_for_prime(x)}")
        if check_for_prime(x):
            prime_sum += x
    return prime_sum


print(add_primes())
