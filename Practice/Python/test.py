import random
slots = {7: " ", 8: " ", 9: " ",
         4: " ", 5: " ", 6: " ",
         1: " ", 2: " ", 3: "x",}

if all(slots.get([1, 3, 7, 9])) == "x":
    print("True")