# -------------------------------------
import random as r
# -------------------------------------
"""HANGMAN GAME"""
# -------------------------------------
'''Data Values'''

words = {
    "DOG": "A man's best friend, most of the time.",
    "CAT": "You don't want to pet its belly.",
    "CAR": "A vehicle.",
    "OTORHINOLARYNGOLOGY": "It is a study of ear, nose, and throat. (Good luck with this one.)",
    "FOOD": "Nourishment eaten in solid form.",
    "METAL": "A music genre.",
    "ARCHITECTURE": "Don't take this career path."
}
word = r.choice(list(words))
guesses = 3
hidden_word = ""  # hidden_word() & hidden_word_new() will fill this up

# -------------------------------------
'''Functions'''

# Word will be hidden by a bunch of dashes (e.g. "Cat" => "---")
def hide_word(x):
    global hidden_word

    # Replaces each letter in hidden_word with dashes
    for _ in list(x):
        hidden_word += '_'
    print(hidden_word)

# Player guesses a letter or word....
def guess():
    global guesses
    global word

    while guesses != 0:
        x = input("\nEnter a letter or word:").upper()
        if len(x.strip()) == 0:
            print("\nYou entered nothing...")
            guess()
        elif x not in list(word):
            print("\nWrong guess...\n")
            hide_word_new(x)
            guesses -= 1
        else:
            print(f'\nYou are correct! "{x}" is in the word...\n')
            hide_word_new(x)

# if guess is already in the hidden_word, and if user has guessed all correct letters
def check_answer():
    pass

# If guess is correct, that letter will not be hidden anymore (e.g. "---"("Cat"), user inputs "a", returns "-a-")
def hide_word_new(answer):
    global word
    global hidden_word

    # Gets the index of guess()
    indices = []
    for index, character in enumerate(word):
        if character == answer:
            indices.append(index)

    # Replaces a hidden_word character to that of guess'
    hidden_word = list(hidden_word)
    for index in indices:
        hidden_word[index] = answer

    hidden_word_new = ""
    for letter in hidden_word:
        hidden_word_new += letter

    # Prints new hidden word
    print(hidden_word_new)

# -------------------------------------
'''Sequence'''
print("HANGMAN!\n")
hide_word(word)
guess()
# -------------------------------------
# changelog:
# 1. Letters will now appear in the empty boxes as you input the right answer
