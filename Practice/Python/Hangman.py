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

def hide_word(x):
    global hidden_word

    # Replaces each letter in hidden_word with dashes
    for _ in list(x):
        hidden_word += '_'

    return hidden_word

def hide_word_new(answer):
    global word
    global hidden_word

    indices = []
    for index, character in enumerate(word):
        if character == answer:
            indices.append(index)

    hidden_word = list(hidden_word)
    for index in indices:
        hidden_word[index] = answer

    hidden_word_new = ""
    for letter in hidden_word:
        hidden_word_new += letter
    hidden_word = hidden_word_new

    return hidden_word

def guess():
    global guesses
    global word

    while guesses != 0:
        if hidden_word == word:
            print("\nYou've won!")
            break
        else:
            x = input("\nEnter a letter or word:").upper()
            if len(x.strip()) == 0:
                print("\nYou entered nothing...")
                guess()
            elif x not in list(word):
                print("\nWrong guess...\n")
                print(hide_word_new(x))
                guesses -= 1
            else:
                print(f'\n"{x}" has been revealed...\n')
                print(hide_word_new(x))

# -------------------------------------
'''Sequence'''
print("HANGMAN!\n")
print(hide_word(word))
guess()
# -------------------------------------
# changelog:
# 1. Letters will now appear in the empty boxes as you input the right answer
# 2. Game can now be won.

# changes to be made:
# 1. Print out the clues
# 2. Print out guess count
# 3.
