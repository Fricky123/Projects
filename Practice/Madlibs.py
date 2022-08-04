import random

num = random.randint(1, 1000)
num1 = 0
num2 = 1000

def intro():
    x = input("Welcome to MadLibs game!\n"
              "Choose an option:\n"
              "[1] Player guesses number\n"
              "[2] Machine guesses number\n"
              "Choice: ")
    if x == "1":
        print("\nNumber is from 1 to 1000...\n"
              "Guess the number...\n")
        Player_Guess_Number()
    elif x == "2":
        print('Type h to say "Higher, l to say "Lower!", or c to say "Correct!\n"')
        Machine_Guess_Number()
    else:
        input("\nInvalid input...")
        print("\n")
        intro()


def Player_Guess_Number():
    global num
    try:
        guess = input("Your guess: ")
        if int(guess) == num:
            print("You're right!!!")
        elif int(guess) <= num:
            print("Higher!\n")
            Player_Guess_Number()
        elif int(guess) >= num:
            print("Lower!\n")
            Player_Guess_Number()
    except ValueError:
        input("\nPlease input only numbers...")
        print("\n")
        Player_Guess_Number()


def Machine_Guess_Number():
    global num1
    global num2
    x = random.randint(num1, num2)
    print(f"Guess: {x}")
    ans = input("answer: ")
    if ans == "l":
        num2 -= (num2 - x)
        num2 -= 1
        Machine_Guess_Number()
    elif ans == "h":
        num1 = x + 1
        Machine_Guess_Number()
    elif ans == "c":
        print("yey im correct!")
    else:
        input("\nInvalid input...")
        print("\n")
        Machine_Guess_Number()


intro()

