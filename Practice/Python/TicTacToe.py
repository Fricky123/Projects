import random
# ---------------------------------------------------------------------

slots = {
    1: " ",
    2: " ",
    3: " ",
    4: " ",
    5: " ",
    6: " ",
    7: " ",
    8: " ",
    9: " "
}

game_Log = []

# ---------------------------------------------------------------------

class Human:

    slots_filled = []

    def __init__(self, shape):
        self.shape = shape

    def draw(self):
        try:
            ans = int(input("Draw where> "))
            if slots.get(ans) == "x" or slots.get(ans) == "o":
                print("Slot already drawn over")
                human.draw()
            else:
                slots.update({ans: human.shape})
                human.slots_filled.append(ans)
                game_Log.append(ans)
        except ValueError:
            input("Please input slot numbers only...")
            human.draw()

class Ai:

    slots_filled = []

    def __init__(self, shape):
        self.shape = shape

    def draw(self):
        ans = random.randint(1, 9)
        if slots.get(ans) == "x" or slots.get(ans) == "o":
            ai.draw()
        else:
            slots.update({ans: ai.shape})
            ai.slots_filled.append(ans)
            game_Log.append(ans)

class Ai_hard:

    slots_filled = []

    def __init__(self, shape):
        self.shape = shape

    def draw(self):
        if Ai_hard == player1:
            ans = random.randint(1, 9)
            if slots.get(ans) == "x" or slots.get(ans) == "o":
                ai.draw()


# ---------------------------------------------------------------------
human = Human(random.choice(["x", "o"]))

if human.shape == "x":
    y = "o"
else:
    y = "x"

ai = Ai(y)

player1 = random.choice([ai, human])
if player1 == human:
    player2 = ai
else:
    player2 = human
# ---------------------------------------------------------------------
def game():

    try:
        while True:
            if player1 == human:
                separate()
                print("Your turn...")
                if not game_Log:
                    print(grid())

            player1.draw()

            if player1 == ai:
                separate()
                print(f'Player 1 has drawn "{ai.shape}" on slot {game_Log.pop()}...')
                print(grid())

            check()
            if check() is False:
                if ai == player1:
                    separate()
                    print('Player 1 Wins')
                else:
                    separate()
                    print(grid())
                    print('You win!')
                break

            if player2 == human:
                separate()
                print("Your turn...")

            player2.draw()

            if player2 == ai:
                separate()
                print(f'Player 2 has drawn "{ai.shape}" on slot {game_Log.pop()}...')

            check()

            if check() is False:
                if ai == player2:
                    separate()
                    print('Player 2 Wins')
                else:
                    separate()
                    print(grid())
                    print('You win!')
                break

            print(grid())


    except RecursionError:
        print(grid())
        print("It's a tie!")

def check():
    win_conditions = [[7, 8, 9], [4, 5, 6], [1, 2, 3], [7, 4, 1], [8, 5, 2], [9, 6, 3], [9, 5, 1], [7, 5, 3]]
    for condition in win_conditions:
        if all([item in human.slots_filled for item in condition]) is True:
            return False
        if all([item in ai.slots_filled for item in condition]) is True:
            return False

def grid():
    return f"| {slots.get(7)} | {slots.get(8)} | {slots.get(9)} |\n" \
           f"| {slots.get(4)} | {slots.get(5)} | {slots.get(6)} |\n" \
           f"| {slots.get(1)} | {slots.get(2)} | {slots.get(3)} |"

def separate():
    print(f"-------------------------------")
# ---------------------------------------------------------------------
print(f"Slot numbers:\n" 
      f"| 7 | 8 | 9 |\n" 
      f"| 4 | 5 | 6 |\n" 
      f"| 1 | 2 | 3 |\n" 
      f"-------------------------------\n" 
      f"Your symbol is {human.shape.upper()}...")
input("Press any key...")



game()
