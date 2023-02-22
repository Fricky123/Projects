import random
import time
# ----------------------------------------------------------------
'''variables'''
slots = {
    1: ' ',
    2: ' ',
    3: ' ',
    4: ' ',
    5: ' ',
    6: ' ',
    7: ' ',
    8: ' ',
    9: ' ',
}
balance = random.randint(100, 1000)
payment = 4
win = 20
# ----------------------------------------------------------------
'''main functions'''
def control():
    global balance
    print(f'Your balance: {balance}')
    act = input(f'Spin the wheel for ${payment}? [y/n]: ').lower()
    if 'y' in act or 'yes' in act:
        balance -= payment
        spin_the_wheels()
        print('[Wheel spinning...]')
        time.sleep(.5)
        grid = f"|{slots.get(7)}|{slots.get(8)}|{slots.get(9)}|\n" \
               f"|{slots.get(4)}|{slots.get(5)}|{slots.get(6)}|\n" \
               f"|{slots.get(1)}|{slots.get(2)}|{slots.get(3)}|"
        print(grid)
        time.sleep(0.2)
        check()
        separate()
        control()
    elif 'n' in act or 'no' in act:
        print('bye!')
        exit()
    else:
        input('[Invalid Input] Press any key to continue> ')
        separate()
        control()

def spin_the_wheels():
    combination1 = ['A', 'B', 'C', 'D', 'E']
    combination2 = ['C', 'B', 'D', 'A', 'E']
    combination3 = ['B', 'A', 'D', 'C', 'E']

    def func1(combination):
        combinations = [[combination[0], combination[1], combination[2]],
                        [combination[1], combination[2], combination[3]],
                        [combination[2], combination[3], combination[4]],
                        [combination[3], combination[4], combination[0]],
                        [combination[4], combination[0], combination[1]]]

        return combinations

    def func2(combination):
        index1 = 0
        index2 = 1
        index3 = 2

        combinations = []

        for letter in combination:
            print(combinations)
            combinations.append([combination[index1], combination[index2], combination[index3]])

            if combinations[index1] == combinations[len(combinations) - 1]:
                index1 = 0
            else:
                index1 += 1

            if combinations[index2] == combinations[len(combinations) - 1]:
                index2 = 0
            else:
                index2 += 1

            if combinations[index3] == combinations[len(combinations) - 1]:
                index3 = 0
            else:
                index3 += 1

        return combinations

    wheel1 = [7, 4, 1]
    wheel2 = [8, 5, 2]
    wheel3 = [9, 6, 3]

    y = random.choice(func1(combination1))
    index = 0
    for number in wheel1:
        slots.update({number: y[index]})
        index += 1

    y = random.choice(func1(combination2))
    index = 0
    for number in wheel2:
        slots.update({number: y[index]})
        index += 1

    y = random.choice(func1(combination3))
    index = 0
    for number in wheel3:
        slots.update({number: y[index]})
        index += 1

def check():
    global balance
    win_conditions = [[7, 8, 9], [4, 5, 6], [1, 2, 3], [7, 4, 1], [8, 5, 2], [9, 6, 3], [9, 5, 1], [7, 5, 3]]

    jackpot = 0
    for condition in win_conditions:
        if slots.get(condition[0]) == slots.get(condition[1]) == slots.get(condition[2]):
            jackpot += 1

    if jackpot:
        if jackpot > 1:
            print(f'You scored {jackpot} points')
        else:
            print(f'You scored {jackpot} point')

        prize = win * jackpot
        balance += prize

        print(f"You won ${prize}!")
    # else:
    #     print('You won nothing!')

def separate():
    print('----------------------------------------------------------------')
# ----------------------------------------------------------------
'''sequence'''
print('3-letter combination = 1 point\n'
      f'1 point = ${win}')
control()

