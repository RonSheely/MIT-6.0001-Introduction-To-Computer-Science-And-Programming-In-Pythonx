def largest_odd_number(*args):
    divisible_by_3 = []
    for number in args:
        if number % 2 != 0:
            divisible_by_3.append(number)
    return max(divisible_by_3)


x = largest_odd_number(1, 5, 7)
print(x)
