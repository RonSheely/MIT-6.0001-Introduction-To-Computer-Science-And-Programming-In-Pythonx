# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : <Ezra Waver>
# Collaborators : <your collaborators>
# Time spent    : <total time>

import math
import random

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3,
    'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}


WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    in_file = open(WORDLIST_FILENAME, 'r')
    wordlist = []
    for line in in_file:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """

    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x, 0) + 1
    return freq


def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

    The score for a word is the product of two components:

    The first component is the sum of the points for letters in the word.
    The second component is the largest of:
    1, or 7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
    and n is the hand length when the word was played

    Letters are scored as in Scrabble; A is worth 1, B is
    worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """
    assert n >= 0, "n must be greater than, or equal to zero."
    word = word.lower()
    first_component = 0
    for char in word:
        first_component += SCRABBLE_LETTER_VALUES.get(char, 0)
    second_component = 7 * len(word) - 3 * (n - len(word))
    if second_component < 1:
        second_component = 1
    return first_component * second_component


def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    
    for letter in hand.keys():
        for j in range(hand[letter]):
            print(letter, end=' ')
    print()


def deal_hand(n, wildcard=True):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    
    hand={}
    num_vowels = int(math.ceil(n / 3))

    vowels_in_hand = []
    for i in range(num_vowels):
        x = random.choice(VOWELS)
        vowels_in_hand.append(x)
        hand[x] = hand.get(x, 0) + 1
    
    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1

    if wildcard is True:
        x = random.choice(vowels_in_hand)
        if hand[x] == 1:
            del hand[x]
            hand["*"] = 1
        else:
            hand[x] -= 1
            hand["*"] = 1

    return hand


def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    hand = hand.copy()
    empty_letters = []
    for char in word:
        char = char.lower()
        try:
            hand[char] -= 1
            if hand[char] == 0:
                empty_letters.append(char)
        except KeyError:
            pass
    for letter in empty_letters:
        del hand[letter]
    return hand


def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    handcopy = hand.copy()

    wild_card_position = 0
    found_in_dict = True
    for x, char in enumerate(word):
        char = char.lower()
        if char == "*":
            wild_card_position = x
        if (char in VOWELS or char in CONSONANTS) is False and char != "*":
            found_in_dict = False
        try:
            if handcopy[char] >= 1:
                handcopy[char] -= 1
            else:
                found_in_dict = False
        except KeyError:
            found_in_dict = False
    word_in_list = (word.lower() in word_list)
    for char in VOWELS:
        test_string = word[:wild_card_position] + char + word[wild_card_position + 1:]
        if test_string in word_list:
            word_in_list = True
    return found_in_dict and word_in_list


def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    letters = 0
    for letter in hand.values():
        letters += letter
    return letters


def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
      
    """
    total_score = 0
    while sum(hand.values()) > 0:
        display_hand(hand)
        user_input = input('Enter word, or "!!" to indicate that you are finished: ')
        if user_input == "!!":
            break
        else:
            if is_valid_word(user_input, hand, word_list):
                earned_points = get_word_score(user_input, sum(hand.values()))
                total_score += earned_points
                print(f'"{user_input}" earned {earned_points}. Total: {total_score}')
            else:
                print("That is not a valid word. Please choose another word")
        hand = update_hand(hand, user_input)
    print(f"Hand over, your score was {total_score}")
    return total_score


def substitute_hand(hand, letter):
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    handcopy = hand.copy()
    letters_in_hand = hand.keys()
    old_letter_value = hand[letter]
    available_letters = [let for let in VOWELS + CONSONANTS if let not in letters_in_hand]
    new_letter = random.choice(available_letters)
    handcopy.pop(letter)
    handcopy[new_letter] = old_letter_value
    return handcopy


def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
      
    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """
    total_score = 0
    letter_subbed = False
    hand_replayed = False
    total_hands = int(input("Enter total number of hands: "))
    for _ in range(total_hands):
        generated_hand = deal_hand(HAND_SIZE)
        if not letter_subbed:
            display_hand(generated_hand)
            sub_letter_input = input("Would you like to substitute a letter? ").lower()
            if sub_letter_input == "yes" or sub_letter_input == "y":
                sub_letter_letter = input("Which letter would you like to replace: ").lower()
                generated_hand = substitute_hand(generated_hand, sub_letter_letter)
                letter_subbed = True
        score = play_hand(generated_hand, word_list)
        if not hand_replayed:
            replay_hand_input = input("Would you like to replay the hand? ")
            if replay_hand_input == "yes" or replay_hand_input == "y":
                score2 = play_hand(generated_hand, word_list)
                total_score += max(score, score2)
        total_score += score
    print(f"Total score over all hands: {total_score}")


if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
