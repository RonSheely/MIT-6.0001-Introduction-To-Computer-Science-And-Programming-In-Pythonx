"""Finger exercise: Write a function to test is_in."""


strings_to_compare = [("Yes", "Yes!", True), ("Nooooo", "Lol", False),
                      ("Si Senor", "Muchas Gracias", False), ("True", "True", True),
                      ("Lol", "lol", False), ("Hola", "Hola Amigo", True), ("Test", "Test", True),
                      ("Nope", "Nuhuh", False), ("Siiiii", "lol", False)]


def is_in(string_a, string_b):
    return string_a in string_b


def test_is_in(test_sample):
    for tup in test_sample:
        result = is_in(tup[0], tup[1])
        if result != tup[2]:
            raise ValueError(f"{tup} returned the wrong expected value")
    print(f"{len(test_sample)} Test(s) ran, no errors found.")


test_is_in(strings_to_compare)
