# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string
import os

VOWELS = ["a", "e", "i", "o", "u"]
ALL_LETTERS = "abcdefghijklmnopqrstuvwxyz"
WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    secret_word_list = list(secret_word)
    for letter in secret_word_list:
        if not letter.lower() in letters_guessed:
            return False
    return True

def get_guessed_word(secret_word, letters_guessed: list):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    guessed_word_blank = list("_" * len(secret_word))
    for letter in letters_guessed:
        for x, char in enumerate(secret_word):
            if char == letter.lower():
                guessed_word_blank[x] = letter.lower()
    return "".join(guessed_word_blank)



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    letters_list = list(ALL_LETTERS)
    for letter in letters_guessed:
        if ALL_LETTERS.find(letter):
            letters_list.remove(letter.lower())
    return "".join(letters_list)


def check_input(message, secret_word, guessed_letters):
    print(message, get_guessed_word(secret_word, guessed_letters))


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    guesses = 6
    warnings = 3
    guessed_letters = []
    guessed = False
    print(f"Im thinking of a word with {len(secret_word)} letters")
    while guesses > 0:
        if warnings == 0:
            print("You used three warnings! you lost a guess!")
            warnings = 3
            guesses -= 1
        guessed = is_word_guessed(secret_word, guessed_letters)
        if guessed is True:
            print("Congrats!, You won!")
            print(f"Your score: {guesses * len(set(secret_word))}")
            return True
        print(f"You Have {guesses} guesses left")
        print(f"You have {warnings} warnings left")
        print(f"Available Letters: {get_available_letters(guessed_letters)}")
        user_guess = input("Please guess a letter: ")[0].lower()
        if user_guess not in ALL_LETTERS:
            warnings -= 1
            check_input("Guess must be a letter:", secret_word, guessed_letters)
            os.system("cls")
            continue
        if user_guess in guessed_letters:
            warnings -= 1
            check_input("Letter already guessed:", secret_word, guessed_letters)
            os.system("cls")
            continue
        guessed_letters.append(user_guess)
        if user_guess in secret_word:
            check_input("Good guess:", secret_word, guessed_letters)
            os.system("cls")
        if user_guess not in secret_word:
            check_input("Oops! That letter is not in my word:", secret_word, guessed_letters)
            os.system("cls")
            if user_guess in VOWELS:
                guesses -= 2
            else:
                guesses -= 1

    print("Sorry! You Lose!")
    print(f"The word was {secret_word}")
    return False

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
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
    '''
    if len(my_word) != len(other_word):
        return False
    for x, char in enumerate(my_word):
        if char != other_word[x] and char != "_":
            return False
    return True


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    found = []
    for word in wordlist:
        if match_with_gaps(my_word, word):
            found.append(word)
    return found

def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    ...
    
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
