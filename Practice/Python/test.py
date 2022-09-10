import random
slots = {
    1: " ",
    2: "o",
    3: " ",
    4: "o",
    5: " ",
    6: " ",
    7: " ",
    8: " ",
    9: "x"
}

current_condition = [7, 8]

for number in current_condition:
    if slots.get(number) == " ":

