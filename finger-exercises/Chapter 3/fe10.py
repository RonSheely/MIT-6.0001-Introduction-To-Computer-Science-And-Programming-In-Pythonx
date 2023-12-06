"""Finger exercise: The Empire State Building is 102 stories high. A
man wanted to know the highest floor from which he could drop an
egg without the egg breaking. He proposed to drop an egg from the
top floor. If it broke, he would go down a floor, and try it again. He
would do this until the egg did not break. At worst, this method
requires 102 eggs. Implement a method that at worst uses seven eggs"""


def run_egg_test(highest_safe_floor: int):
    print(f"The egg can safely drop from floor {highest_safe_floor}, let the science begin!")
    floors = 102
    eggs_used = 0
    low = 1
    high = max(low, floors)
    current_floor = round((high + low) / 2)
    while True:
        eggs_used += 1
        print(f"The man drops the egg from floor {current_floor}... He's used {eggs_used} egg(s)")
        if current_floor > highest_safe_floor:
            high = current_floor
            print("SPLAT! The egg breaks!")
        else:
            low = current_floor
        current_floor = round((high + low) / 2)
        if high - 1 == low or current_floor >= floors:
            break
    print(f"The egg survives on floor {current_floor}, what a breakthrough!")


def main():
    run_egg_test(101)


if __name__ == "__main__":
    main()
