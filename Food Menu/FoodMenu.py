"""A practice simulation that lets users order food"""
"""WIP WIP WIP WIP"""
import random

Costs = 0
Items = 0
List = []
Customer_Money = random.randint(500, 1000)

# Food
f = {"f1": "Adobo",
     "f2": "Sinigang",
     "f3": "Pakbet",
     "f4": "Kinilaw",
     "f5": "Bulalo"}

# Prices for Food
f_p = {"f1": 50,
       "f2": 60,
       "f3": 334345,
       "f4": 234,
       "f5": 133}


def intro():
    """Introductory script"""

    print("Welcome to McFricky\n")

    x = input("Would you like to order[y/n]? ")

    if x == "y":
        menu()

    elif x == "n":
        print("\nGoodbye!")

    else:
        input("Invalid input...\n")
        intro()


def menu():
    """Provides customer with a list of choices"""

    print("\n"
          "Your cart:\n\n"
          f"Cost: {Costs} php\n"
          f"Items: {Items}")

    if not List:
        print(f"List: none\n")
    else:
        print(f"List: {List}\n")

    print(f"Your balance: {Customer_Money} php\n"
          "\nOptions: [1]Food Menu, [2]Purchase orders, [3] Exit")

    x = input("\nEnter number of choice: ")

    if x == "1":
        ordering()

    elif x == "2":
        print(f"You new balance: {Customer_Money - Costs}")
        y = input("Finalize purchase[y/n]? ")


    elif x == "3":
        print("Goodbye...")

    else:
        input("Invalid input...")
        menu()


def ordering():
    """Provides customer with a list of choices for food"""
    print(f"\n"
          f"[1]{f.get('f1')} = {f_p.get('f1')} php\n"
          f"[2]{f.get('f2')} = {f_p.get('f2')} php\n"
          f"[3]{f.get('f3')} = {f_p.get('f3')} php\n"
          f"[4]{f.get('f4')} = {f_p.get('f4')} php\n"
          f"[5]{f.get('f5')} = {f_p.get('f5')} php\n"
          f"[6]Exit"
          f"\n")
    x = input("Input order: ")
    if x == "1":
        transaction("f1")
    elif x == "2":
        transaction("f2")
    elif x == "3":
        transaction("f3")
    elif x == "4":
        transaction("f4")
    elif x == "5":
        transaction("f5")
    elif x == "6":
        print("Exiting Food Menu...")
        menu()
    else:
        input("Invalid input...")
        ordering()


def transaction(x):
    """Make changes to COSTS/ITEMS/LIST in customer's CART"""

    global Costs
    global Items

    print(f"{f.get(x)} selected...")

    try:
        quantity = int(input("Input quantity: "))

        print(f"{quantity} {f.get(x)} ordered...")

        y = input("Add to cart[y/n]?: ")

        if y == "y":
            Costs += quantity * f_p.get(x)
            Items += quantity
            List.append(f"{f.get(x)}({quantity})")
            menu()

        elif y == "n":
            print("\nOrder cancelled...")
            ordering()

        else:
            input("Invalid input...")
            ordering()

    except ValueError:
        input("Invalid; please use whole numbers as input...")
        ordering()


# Sequence
intro()
