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

        if not game_Log:
            print(grid())

        try:
            ans = int(input("Draw where> "))
            if slots.get(ans) == "x" or slots.get(ans) == "o":
                print("Slot already drawn over")
                user.draw()
            elif len(str(ans)) == 1:
                slots.update({ans: user.shape})
                user.slots_filled.append(ans)
                game_Log.append(ans)
                print(f"You drew {user.shape} on slot {game_Log[-1:][0]}...")
                print(grid())

        except ValueError:
            input("Please input slot numbers only...")
            user.draw()

class AI_Easy:
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
            time.sleep(0.9)
            print(f"Opponent drew {ai.shape} on slot {game_Log[-1:][0]}...")

            print(grid())

class AI_Mid:
    slots_filled = []
    shape = None

    def draw(self):
        bestScore = -1000
        bestMove = 0

        for space in slots.keys():
            pass

        # if slots.get(ans) == "x" or slots.get(ans) == "o":
        #     ai.draw()
        # else:
        #     slots.update({ans: ai.shape})
        #     ai.slots_filled.append(ans)
        #     game_Log.append(ans)
        #     print(f"Opponent drew {ai.shape} on slot {game_Log[-1:][0]}...")
        #     print(grid())

class AI_Hard:
    slots_filled = []
    shape = None

    def draw(self):
        pass

user = Human()
player1 = None
player2 = None
# ---------------------------------------------------------------------
def choose_difficulty():
    x = input("[E]asy, [M]edium, Or [H]ard difficulty: ").lower()
    if "easy" in x or "e" in x:
        return AI_Easy
    elif "medium" in x or "m" in x:
        return AI_Mid
    elif "hard" in x or "h" in x:
        return AI_Hard

ai = choose_difficulty()()

def assign_player():
    global user, ai, player1, player2

    player1 = random.choice([user, ai])
    if player1 == user:
        player2 = ai
    else:
        player2 = user

    player1.shape = random.choice(["o", "x"])
    if player1.shape == "x":
        player2.shape = "o"
    else:
        player2.shape = "x"

def intro():
    separate()
    if user == player1:
        print(f"You are player 1!")
    else:
        print(f"You are player 2!")
    print(f"Your shape is '{user.shape.upper()}'")
    separate()
    print(f"Slot numbers:\n"
          f"| 7 | 8 | 9 |\n"
          f"| 4 | 5 | 6 |\n"
          f"| 1 | 2 | 3 |\n"
          f'Tip: use the keypad as "controls"')
    separate()
    input("Press any key to continue...")
    separate()

def game():

    while True:

        player1.draw()
        check()
        if check() == "user_win":
            print("You won!")
            break
        elif check() == "ai_win":
            print("Opponent Won")
            break
        elif check() == "tie":
            print("It's a tie!")
            break

        player2.draw()
        check()
        if check() == "user_win":
            print("You won!")
            break
        elif check() == "ai_win":
            print("Opponent Won")
            break
        elif check() == "tie":
            print("It's a tie!")
            break

def check():
    win_conditions = [[7, 8, 9], [4, 5, 6], [1, 2, 3], [7, 4, 1], [8, 5, 2], [9, 6, 3], [9, 5, 1], [7, 5, 3]]
    for condition in win_conditions:
        if all([item in user.slots_filled for item in condition]) is True:
            return "user_win"
        elif all([item in ai.slots_filled for item in condition]) is True:
            return "ai_win"

    if len(game_Log) == 9:
        return "tie"

def grid():
    return f"| {slots.get(7)} | {slots.get(8)} | {slots.get(9)} |\n"\
           f"| {slots.get(4)} | {slots.get(5)} | {slots.get(6)} |\n"\
           f"| {slots.get(1)} | {slots.get(2)} | {slots.get(3)} |"

def separate():
    print(f"-------------------------------")
# ---------------------------------------------------------------------
assign_player()
intro()
game()
