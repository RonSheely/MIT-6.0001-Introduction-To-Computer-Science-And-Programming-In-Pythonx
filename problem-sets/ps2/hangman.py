import random
import os
import time

VOWELS = ["a", "e", "i", "o", "u"]
ALL_LETTERS = "abcdefghijklmnopqrstuvwxyz"
WORDLIST_FILENAME = "words.txt"
SLEEP_CONSTANT = 1.2


def clean_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def load_words(word_file):
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    # print("Loading word list from file...")
    in_file = open(word_file, 'r')
    line = in_file.readline()
    wordlist = line.split()
    # print("  ", len(wordlist), "words loaded.")
    return wordlist


LOADED_WORDLIST = load_words(WORDLIST_FILENAME)


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


def is_word_guessed(secret_word, letters_guessed):
    """
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    """
    secret_word_list = list(secret_word)
    for letter in secret_word_list:
        if not letter.lower() in letters_guessed:
            return False
    return True


def get_guessed_word(secret_word, letters_guessed: list):
    """
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
    which letters in secret_word have been guessed so far.
    """
    guessed_word_blank = list("_" * len(secret_word))
    for letter in letters_guessed:
        for x, char in enumerate(secret_word):
            if char == letter.lower():
                guessed_word_blank[x] = letter.lower()
    return "".join(guessed_word_blank)


def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    """
    letters_list = list(ALL_LETTERS)
    for letter in letters_guessed:
        letters_list.remove(letter.lower())
    return "".join(letters_list)


def match_with_gaps(my_word, other_word):
    """
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns:
        boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    example:
        my_word = b_b, other_word = bob
        returns True
    """
    if len(my_word) != len(other_word):
        return False
    for x, char in enumerate(my_word):
        if char != other_word[x] and char != "_":
            return False
    return True


def show_possible_matches(my_word):
    """
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    """
    found = []
    for word in LOADED_WORDLIST:
        if match_with_gaps(my_word, word):
            found.append(word)
    return found


def play_hangman(secret_word, allow_hints=True):
    clean_screen()
    print("Welcome to the game Hangman!")
    print(f"Im thinking of a word with {len(secret_word)} letters.\n")

    guesses = 6
    warnings = 3
    guessed_letters = []
    guessed_word = get_guessed_word(secret_word, guessed_letters)
    available_letters = get_available_letters(guessed_letters)
    while guesses > 0:
        if guessed_word == secret_word:
            break
        print(f"The word is: {guessed_word}\n")
        print(f"You have {guesses} guesses remaining.")
        print(f"Available letters: {available_letters}")
        try:
            user_input = input("Please guess a letter: ")[0].lower()
        except IndexError:
            clean_screen()
            continue
        if user_input == "*" and allow_hints:
            results = show_possible_matches(get_guessed_word(secret_word, guessed_letters))
            formatted_results = [entry + ("," if i % 5 != 0 or i == len(results) else "\n")
                                 for i, entry in enumerate(results, 1)]
            if len(results) > 40:
                clean_screen()
                print("Too many possiblities! try again later...")
                time.sleep(SLEEP_CONSTANT)
                clean_screen()
            else:
                clean_screen()
                print("Possible word matches are:")
                print(" ".join(formatted_results))
                print(f"\nYour Word: \n{get_guessed_word(secret_word, guessed_letters)}")
                time.sleep(2)
                clean_screen()
            continue
        if user_input not in ALL_LETTERS:
            warnings -= 1
            clean_screen()
            print(f"\nOops! That is not a valid letter. You have {warnings} warnings left.")
            time.sleep(SLEEP_CONSTANT)
            clean_screen()
            continue
        if user_input in guessed_letters:
            warnings -= 1
            clean_screen()
            print(f"Oops! You already guessed that letter. {warnings} warnings remain.")
            time.sleep(SLEEP_CONSTANT)
            clean_screen()
            continue
        guessed_letters.append(user_input)
        guessed_word = get_guessed_word(secret_word, guessed_letters)
        available_letters = get_available_letters(guessed_letters)
        if user_input in secret_word:
            clean_screen()
            print(guessed_word)
            print("Good guess!")
            time.sleep(SLEEP_CONSTANT)
            clean_screen()
        else:
            clean_screen()
            print(guessed_word)
            print("Oops! That letter is not in my word.")
            time.sleep(SLEEP_CONSTANT)
            clean_screen()
            if user_input in VOWELS:
                guesses -= 2
            else:
                guesses -= 1
    print(f'The word was "{secret_word}!"')
    if guessed_word == secret_word:
        print("Congratulations! You won!")
        print(f"Your score was: {guesses * len(set(secret_word))}")
    else:
        print("Better luck next time!")


if __name__ == "__main__":
    chosen_word = choose_word(LOADED_WORDLIST)
    play_hangman(chosen_word)
