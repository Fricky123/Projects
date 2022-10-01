import random
import time
# ---------------------------------------------------------------------
'''game data'''

slots = {7: " ", 8: " ", 9: " ",
         4: " ", 5: " ", 6: " ",
         1: " ", 2: " ", 3: " ",}

game_Log = []
# ---------------------------------------------------------------------
'''player classes'''
class Human:
    slots_filled = []
    shape = None

    def draw(self):

        if not game_Log:
            print(grid())
        ans = None
        try:
            ans = int(input("Draw where> "))
            if len(str(ans)) > 1:
                invalid()
                user.draw()
            elif slots.get(ans) != " ":
                print("Slot is occupied... Try again...")
                time.sleep(0.5)
                print(grid())
                user.draw()
            else:
                slots.update({ans: user.shape})
                user.slots_filled.append(ans)
                game_Log.append(ans)
                print(f"You drew {user.shape} on slot {game_Log[-1]}...")
                print(grid())

        except ValueError:
            if ans is None:
                input("You entered nothing...")
            else:
                input("Please input slot numbers only...")
            user.draw()

class AI_Easy:

    slots_filled = []
    shape = None

    def draw(self):

        def confirm_move(move):
            slots.update({move: ai.shape})
            ai.slots_filled.append(move)
            game_Log.append(move)
            time.sleep(0.9)
            print(f"Opponent drew {ai.shape} on slot {game_Log[-1]}...")
            print(grid())

        x = random.randint(1, 9)
        if slots.get(x) != " ":
            ai.draw()
        else:
            confirm_move(x)

class AI_Mid:
    slots_filled = []
    shape = None

    my_conditions = []
    current_condition = []
    win_conditions = [[7, 8, 9], [4, 5, 6], [1, 2, 3], [7, 4, 1], [8, 5, 2], [9, 6, 3], [9, 5, 1], [7, 5, 3]]
    def draw(self):
        def confirm_move(move):
            slots.update({move: ai.shape})
            ai.slots_filled.append(move)
            game_Log.append(move)
            time.sleep(0.9)
            print(f"Opponent drew {ai.shape} on slot {game_Log[-1]}...")
            print(grid())

        def func1():
            corners = [1, 3, 7, 9]
            x = None
            for num in corners:
                if num in self.current_condition:
                    x = num
            if x is None:
                x = random.choice(self.current_condition)

            if slots.get(self.current_condition[0]) == user.shape or slots.get(self.current_condition[-1]) == user.shape:
                self.my_conditions.remove(self.current_condition)
                self.current_condition = []
                cycle()
            else:
                self.current_condition.remove(x)
                confirm_move(x)

                for condition in self.win_conditions:
                    if x in condition:
                        condition.remove(x)
                        self.my_conditions.append(condition)

        def func2():
            x = random.choice(self.my_conditions)
            self.current_condition = x
            cycle()

        def func3():
            x = []
            if slots.get(1) == " ":
                x.append(1)
            if slots.get(3) == " ":
                x.append(3)
            if slots.get(7) == " ":
                x.append(7)
            if slots.get(9) == " ":
                x.append(9)
            if not x:
                x = 0
                while slots.get(x) != " ":
                    x = random.randint(1, 9)
            else:
                x = random.choice(x)

            confirm_move(x)

            for condition in self.win_conditions:
                if x in condition:
                    condition.remove(x)
                    self.my_conditions.append(condition)

        def cycle():
            if not self.current_condition and not self.my_conditions:
                func3()

            elif not self.current_condition and self.my_conditions:
                func2()

            elif self.current_condition and self.my_conditions:
                func1()

        cycle()

class AI_Hard:
    slots_filled = []
    shape = None

    def draw(self):
        pass

user = Human()
ai = None
player1 = None
player2 = None

# ---------------------------------------------------------------------
'''functions'''

def resetEverything():
    global slots, game_Log
    slots = {7: " ", 8: " ", 9: " ",
             4: " ", 5: " ", 6: " ",
             1: " ", 2: " ", 3: " ", }
    game_Log = []

    # human
    Human.slots_filled = []
    Human.shape = None

    # easy
    AI_Easy.slots_filled = []
    AI_Easy.shape = None

    # medium
    AI_Mid.slots_filled = []
    AI_Mid.shape = None
    AI_Mid.my_conditions = []
    AI_Mid.current_condition = []
    AI_Mid.win_conditions = [[7, 8, 9], [4, 5, 6], [1, 2, 3], [7, 4, 1], [8, 5, 2], [9, 6, 3], [9, 5, 1], [7, 5, 3]]

def choose_difficulty():
    global ai
    x = input("[1]Easy | [2]Medium | [3]Hard\n"
              ">  ").lower()
    if x.isnumeric() is True and len(x) > 1:
        input("Please input only one number of choice...")
        choose_difficulty()
    elif "easy" in x or "1" in x:
        ai = AI_Easy()
    elif "medium" in x or "2" in x:
        ai = AI_Mid()
    elif "hard" in x or "3" in x:
        ai = AI_Hard()
    else:
        input("Invalid input...")
        separate()
        choose_difficulty()

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
    def check():
        win_conditions = [[7, 8, 9], [4, 5, 6], [1, 2, 3], [7, 4, 1], [8, 5, 2], [9, 6, 3], [9, 5, 1], [7, 5, 3]]
        for condition in win_conditions:
            if all([item in user.slots_filled for item in condition]) is True:
                return "user_win"
            elif all([item in ai.slots_filled for item in condition]) is True:
                return "ai_win"

        if len(game_Log) == 9:
            return "tie"
    def declare():
        def decide():
            ans = input("Do you want to play again? ").lower()
            if 'yes' in ans:
                separate()
                sequence()
            elif 'no' in ans:
                exit()
            else:
                invalid()
                decide()

        if check():
            if check() == "user_win":
                print("You won!")

            elif check() == "ai_win":
                print("Opponent Won!")

            elif check() == "tie":
                print("It's a tie!")

            separate()
            decide()

    while True:
        # print(AI_Mid.my_conditions)
        # print(AI_Mid.win_conditions)
        player1.draw()
        check()
        declare()
        # print(AI_Mid.my_conditions)
        # print(AI_Mid.win_conditions)
        player2.draw()
        check()
        declare()

# ---------------------------------------------------------------------
'''utility functions'''

def grid():
    return f"| {slots.get(7)} | {slots.get(8)} | {slots.get(9)} |\n"\
           f"| {slots.get(4)} | {slots.get(5)} | {slots.get(6)} |\n"\
           f"| {slots.get(1)} | {slots.get(2)} | {slots.get(3)} |"

def separate():
    print(f"-------------------------------")

def invalid():
    input("Please input a valid answer... Press any key to continue... ")
# ---------------------------------------------------------------------
'''sequence'''
def sequence():
    resetEverything()
    choose_difficulty()
    assign_player()
    intro()
    game()

sequence()
