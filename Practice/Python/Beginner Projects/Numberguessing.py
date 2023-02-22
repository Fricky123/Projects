import random
import string

number = random.randint(1, 100)

ai_highest_guess = 100
ai_lowest_guess = 1

def intro():
    print("[1]You guess the number, [2]Computer guesses the number")
    x = input("> ")
    if not x or x == " ":
        print('You entered nothing')
        intro()
    elif x == "1":
        func1()
    elif x == "2":
        func2()

def func1():
    try:
        x = int(input('Guess the number: '))
        if not x or x == " ":
            print('You entered nothing')
            func1()
        elif x > number:
            print('lower!')
        elif x < number:
            print('higher')
        elif x == number:
            print('correct')
            exit()
    except ValueError:
        print('error')

    func1()

def func2():
    global ai_lowest_guess, ai_highest_guess
    guess = 0
    x = 0
    ceiling = False
    try:
        x = int(input("What is your secret number? "))
        if not x or x == " ":
            input('error')
            func2()
    except ValueError:
        input('error')
        func2()
    print(f"Secret Number: {x}")
    while True:
        guess = random.randint(ai_lowest_guess, ai_highest_guess)
        print(f'Computer guess: {guess}')
        if guess == x:
            print('test ai win')
            exit()
        y = input("Higher or lower: ")
        if "higher" in y or '2' in y:
            ai_lowest_guess = guess + 1
            if ceiling is False:
                ai_highest_guess *= 2
        elif "lower" in y or '1' in y:
            ai_highest_guess = guess - 1
            ceiling = True
        else:
            print('error')
intro()





