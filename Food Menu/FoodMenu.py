'''A automated machine that lets custormers order food'''
import random

Customer_Money = 0


def intro():
    '''Introductory script'''
    print("Welcome to McFricky\n")
    x = input("Would you like to order? ")
    if x == "y":
        ordering()
    elif x == "n":
        print("\nGoodbye!")
    else:
        input("Invalid input...")
        intro()

def menu():
    '''Provides customer with a list of choices for food'''
    print("")

def ordering():
    '''Provides customer with a list of choices'''
    print("[1] Food Menu, [2] Purchase orders, [3] Exit\n")
    x = input("Enter number of choice: ")
    if x == "1":
        pass
    elif x == "2":
        pass
    elif x == "3":
        pass
    else:
        input("Invalid input...")
        ordering()


def transaction(x):
    '''Make changes to COSTS/ITEMS/LIST of customer's CART'''


# Sequence
Customer_Money = random.randint(500, 1000)
intro()
