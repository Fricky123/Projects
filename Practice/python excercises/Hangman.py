"""Hangman"""
from random_word import RandomWords
# ---------------------------------------------------
'''Variables'''
word = RandomWords()

# ---------------------------------------------------
'''Main Functions (In Order)'''
def intro():
    """Introduces player to the game"""
    print("Do you want to play a game of Hangman?")
    x = input("[y/n]: ")
    if x == "y":
        word.get_random_word()
        # func1(word)
    elif x == "n":
        pass
    else:
        pass
def func1(x):
    word_list = list(x)
    unknown = ""
    for y in word_list:
        unknown += "-"
    print(word)
    print(unknown)
# ---------------------------------------------------
'''Utility Functions'''

def invalid():
    input("Invalid input....")

# ---------------------------------------------------
'''Sequence'''
# intro()
word.get_random_word()
