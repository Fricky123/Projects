import random

from django.template.defaultfilters import lower

Moves = ["Rock", "Scissors", "Paper"]


def game(First_Player, Second_Player):
    if First_Player == "rock" and Second_Player == "Scissors":
        print("Player wins!")
    elif First_Player == "rock" and Second_Player == "Paper":
        print("Computer wins!")
    elif First_Player == "scissors" and Second_Player == "Paper":
        print("Player wins!")
    elif First_Player == "scissors" and Second_Player == "Rock":
        print("Computer wins!")
    elif First_Player == "paper" and Second_Player == "Rock":
        print("Player wins!")
    elif First_Player == "paper" and Second_Player == "Scissors":
        print("Computer wins!")
    elif First_Player == Second_Player:
        print("It's a tie!")
    else:
        input("You entered a wrong input. You're disqualified!\n"
              "Computer wins!")


# Sequence
x = lower(input("Choose between Rock, Paper, or Scissors...\n"
                "Select Move: "))
y = random.choice(Moves)
print(f"Computer's Move: {y}")
game(x, y)