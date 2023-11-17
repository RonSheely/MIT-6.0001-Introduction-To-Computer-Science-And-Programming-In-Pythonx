x = int(input('Enter an integer greater than 2: '))
smallest_divisor = 0
for guess in range(2, x):
    if x % guess == 0:
        smallest_divisor = guess
        largest_divisor = int(x / guess)
        break
if smallest_divisor != 0:
    print("Smallest divisor of", x, 'is', smallest_divisor)
    print("Largest divisor of", x, 'is', largest_divisor)
else:
    print(x, 'is a prime number')
