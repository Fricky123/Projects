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
    "OTORHINOLARYNGOLOGY": "It is a study of ear, nose, and throat.",
    "FOOD": "Nourishment eaten in solid form.",
    "METAL": "A music genre.",
    "ARCHITECTURE": "Don't take this career path.",
    "PROGRAMMING": "Sakit sa ulo, di ko kasabot",
    "FRICKY": "The person who made this... :)"
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
            if guesses == 1:
                x = input(f"Enter a letter or word(Last Try): ").upper()
            else:
                x = input(f"Enter a letter or word({guesses} tries left): ").upper()
            if len(x.strip()) == 0:
                print("You entered nothing...")
                guess()
            elif x in hidden_word:
                print(f"{x} is already guessed...")
            elif x == word:
                print("\n" + word)
                print("\nYou've won!")
                break
            elif x not in list(word):
                print("Wrong guess...")
                guesses -= 1
            else:
                print("\n"+hide_word_new(x))

    if guesses == 0:
        print("You have ran out of guesses... You lost.")
# -------------------------------------
'''Sequence'''
print("HANGMAN!\n")
print(hide_word(word))
print("\nClue: " + words.get(word))
guess()
# -------------------------------------
# changelog:
# 1. Letters will now appear in the empty boxes as you input the right answer
# 2. Game can now be won.
# 3. Printed clues & guesses

