Word = "HANGMAN"
Letters = []
Letters_Hidden = []

def machine(guess):
    global Word_Hidden
    index = 0
    for i in range(len(Word)):
        if Word[i] == guess:
            index = i
    print(index)

for letter in Word:
    Letters.append(letter)
    Letters_Hidden.append("-")

Word_Hidden = " ".join(Letters_Hidden)

print(f"Guess this word: {Word_Hidden}")
x = input("Input: ")
machine(x.upper())

# Letters_Hidden[5] = Letters[5]
#
# Word_Hidden = "".join(Letters_Hidden)
#
# print(Word_Hidden)
