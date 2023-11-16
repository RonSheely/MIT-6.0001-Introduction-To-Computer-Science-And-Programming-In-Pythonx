def largest_odd_number(*args):
    divisible_by_3 = []
    for number in args:
        if number % 2 != 0:
            divisible_by_3.append(number)
    if not divisible_by_3:
        return_value = None
    else:
        return_value = max(divisible_by_3)
    return return_value


print(largest_odd_number(6, 4, 2, 8, 10, 12, 4))
