"""Finger exercise: Write a program that prints the sum of the prime
numbers greater than 2 and less than 1000. Hint: you probably want
to have a loop that is a primality test nested inside a loop that
iterates over the odd integers between 3 and 999"""


def is_odd_prime(input_int: int) -> bool:
    for x in range(3, input_int-1, 2):
        if input_int % x == 0:
            return False
    return True


def calc_odd_primes():
    list_of_odd_primes = []
    for x in range(3, 999, 2):
        if is_odd_prime(x) is True:
            list_of_odd_primes.append(x)
    return list_of_odd_primes


def print_int_list(ints: list):
    for number in ints:
        print(number)


def main():
    result = calc_odd_primes()
    print_int_list(result)


if __name__ == "__main__":
    main()
