"""Finger exercise: Write a program that asks the user to enter an
integer and prints two integers, root and pwr, such that 1 < pwr < 6
and root**pwr is equal to the integer entered by the user. If no such
pair of integers exists, it should print a message to that effect."""


def get_root_and_power(user_number: int) -> tuple:
    for x in range(2, user_number):
        for y in range(2, 7):
            if x**y == user_number:
                return x, y
    return 0, 0


def main():
    gain_input = int(input("Please enter a number to be tested: "))
    result = get_root_and_power(gain_input)
    if result == (0, 0):
        print("root**power does not exist for your integer, unless power > 6, or power < 1")
    else:
        print(f"The resulting equation for your integer is {result[0]}**{result[1]}")


if __name__ == "__main__":
    main()
