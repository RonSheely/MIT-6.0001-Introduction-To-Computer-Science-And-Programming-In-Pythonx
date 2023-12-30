"""Finger exercise: Write a program that first stores the first ten
numbers in the Fibonnaci sequence to a file named fib_file. Each
number should be on a separate line in the file. The program should
then read the numbers from the file and print them"""

FILE_NAME = "fe29_fib_file"


def fib(x: int):
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x - 1) + fib(x - 2)


with open(FILE_NAME, "w") as file:
    for i in range(1, 10 + 1):
        file.write(str(fib(i)) + "\n")


with open(FILE_NAME, "r") as file:
    for line in file:
        print(line.strip("\n"))
