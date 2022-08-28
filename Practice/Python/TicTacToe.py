import random
import time
# ---------------------------------------------------------------------
'''Game Data'''

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
'''Player Classes'''
class Human:

    slots_filled = []
    shape = None

    def draw(self):
        try:
            ans = int(input("Draw where> "))
            if slots.get(ans) == "x" or slots.get(ans) == "o":
                print("Slot already drawn over")
                human.draw()
            elif len(str(ans)) == 1:
                slots.update({ans: human.shape})
                human.slots_filled.append(ans)
                game_Log.append(ans)
            else:
                invalid()
                grid()
                human.draw()
        except ValueError:
            input("Please input slot numbers only...")
            grid()
            human.draw()

class Ai:

    slots_filled = []
    shape = None

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
    shape = None

    def draw(self):
        pass
        # if not game_Log:
        #     ans = random.choice([1, 3, 7, 9])
        #     if slots.get(ans) == "x" or slots.get(ans) == "o":
        #         ai.draw()
        #     else:
        #         slots.update({ans: ai.shape})
        #         ai.slots_filled.append(ans)
        #         game_Log.append(ans)
        #
        # elif


class Ai_impossible:
    pass

# ---------------------------------------------------------------------
'''Functions in order'''
def intro():
    print("Welcome to the TicTacToe game!\n\n"
          "[1]Easy [2]Hard [3]Impossible")
    ans = input("Select difficulty> ")
    if ans == "1":
        separate()
        print("Easy difficulty selected...")
        separate()
        return Ai()
    if ans == "2":
        separate()
        print("Hard difficulty selected...")
        separate()
        return Ai_hard()
    if ans == "3":
        separate()
        print("Impossible difficulty selected...")
        separate()
        return Ai_impossible()

def game():

    try:
        while True:
            if player1 == human:
                separate()
                if not game_Log:
                    grid()
                else:
                    print("Your turn...")

            time.sleep(0.1)
            player1.draw()

            if player1 == ai:
                separate()
                print(f'Player 1 has drawn "{ai.shape}" on slot {game_Log.pop()}...')
                grid()

            check()
            if check() is False:
                if ai == player1:
                    separate()
                    print('Player 1 Wins')
                else:
                    separate()
                    grid()
                    print('You win!')
                break

            if player2 == human:
                separate()
                print("Your turn...")

            time.sleep(0.1)
            player2.draw()

            if player2 == ai:
                separate()
                print(f'Player 2 has drawn "{ai.shape}" on slot {game_Log.pop()}...')

            check()

            if check() is False:
                if ai == player2:
                    separate()
                    print('Player 2 Won')
                else:
                    separate()
                    grid()
                    print('You won!')
                break

            grid()


    except RecursionError:
        grid()
        print("It's a tie!")

def check():
    win_conditions = [[7, 8, 9], [4, 5, 6], [1, 2, 3], [7, 4, 1], [8, 5, 2], [9, 6, 3], [9, 5, 1], [7, 5, 3]]
    for condition in win_conditions:
        if all([item in human.slots_filled for item in condition]) is True:
            return False
        if all([item in ai.slots_filled for item in condition]) is True:
            return False

def grid():
    print(f"| {slots.get(7)} | {slots.get(8)} | {slots.get(9)} |\n"
          f"| {slots.get(4)} | {slots.get(5)} | {slots.get(6)} |\n"
          f"| {slots.get(1)} | {slots.get(2)} | {slots.get(3)} |")

def separate():
    print(f"-------------------------------")

def invalid():
    input("Invalid input....")
# ---------------------------------------------------------------------
'''Sequence'''
human = Human()
ai = intro()
human.shape = random.choice(["x", "o"])
if human.shape == "x":
    y = "o"
else:
    y = "x"
ai.shape = y
player1 = random.choice([ai, human])
if player1 == human:
    player2 = ai
else:
    player2 = human
time.sleep(0.3)
print(f"Slot numbers:\n" 
      f"| 7 | 8 | 9 |\n" 
      f"| 4 | 5 | 6 |\n" 
      f"| 1 | 2 | 3 |\n" 
      f"-------------------------------\n" 
      f"Your symbol is {human.shape.upper()}...")
if human == player1:
    print("You are player 1...")
else:
    print("You are player 2...")
input("Press any key...")
game()
