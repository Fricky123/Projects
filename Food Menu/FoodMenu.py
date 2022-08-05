import random

"""Online Order simulation"""

# ----------------------------------------------------------------------
'''global variables'''

# Cart
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

# Miscellaneous
Delivery_Cost = 9999

# ----------------------------------------------------------------------
'''Main Functions (in order)'''

def intro():
    """Introductory script"""
    separator_line()

    print("Welcome to McFricky!\n")

    x = input("Would you like to order[y/n]? ")

    if x == "y":
        menu()

    elif x == "n":
        separator_line()
        print("Goodbye!")
        separator_line()

    else:
        invalid_input()
        intro()

def menu():
    """Provides customer with a list of choices"""
    separator_line()
    customer_cart()

    print("Options: [1]Food Menu, [2]Purchase/Reset Cart, [3] Exit")

    x = input("Choose option: ")

    if x == "1":
        ordering()

    elif x == "2":
        cart_menu()

    elif x == "3":
        separator_line()
        y = input("Exit to Main Menu[y/n]: ")

        if y == "y":
            intro()

        elif y == "n":
            menu()

        else:
            invalid_input()
            menu()

    else:
        invalid_input()
        menu()

def ordering():
    """Provides customer with a list of choices for food"""

    separator_line()

    print(f"\n"
          f"[1]{f.get('f1')} = {f_p.get('f1')} php\n"
          f"[2]{f.get('f2')} = {f_p.get('f2')} php\n"
          f"[3]{f.get('f3')} = {f_p.get('f3')} php\n"
          f"[4]{f.get('f4')} = {f_p.get('f4')} php\n"
          f"[5]{f.get('f5')} = {f_p.get('f5')} php\n"
          f"[6]Exit\n")

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
        print("(Exiting Food Menu...)")
        menu()

    else:
        invalid_input()
        ordering()

def transaction(x):
    """Make changes to COSTS/ITEMS/LIST in customer's CART based on his order"""
    separator_line()

    global Costs
    global Items

    print(f"{f.get(x)} selected...")

    separator_line()

    try:
        quantity = int(input("Input quantity: "))

        print(f"You are about to add {quantity} order/s of {f.get(x)} to you Cart...")

        y = input("Add to cart[y/n]?: ")

        if y == "y":
            Costs += quantity * f_p.get(x)
            Items += quantity
            List.append(f"{f.get(x)}({quantity})")

            separator_line()

            print(f"{quantity} order/s of {f.get(x)} added to Cart...")

            menu()

        elif y == "n":
            separator_line()
            print("\nOrder cancelled...\n")
            ordering()

        else:
            input("--------------------------------------------------\n"
                  "Invalid input... Press any key to continue...")
            print("(Please use whole numbers for this input)"
                  "-----------------------------------")
            ordering()

    except ValueError:
        input("--------------------------------------------------\n"
              "Invalid input... Press any key to continue...")
        print("(Please use whole numbers for this input)"
              "-----------------------------------")
        ordering()

# ----------------------------------------------------------------------
'''Utility Functions'''

def customer_cart():
    if not List and not Items:
        print("Your Cart:\n\n"
              f"Cost: 0 php\n"
              f"Items: none\n"
              f"List: none\n\n"
              f"Your balance: {Customer_Money} php\n")

    else:
        print("Your Cart:\n\n"
              f"Cost: {Costs} php\n"
              f"Items: {Items}\n"
              f"List: {List}\n\n"
              f"Your balance: {Customer_Money} php\n")


def cart_menu():
    global Costs
    global Items
    global List

    separator_line()

    if Items:
        customer_cart()

        print("[1]Purchase [2]Reset [3]Exit")

        y = input("Choose option: ")

        if y == "1":
            if Customer_Money < (Costs + Delivery_Cost):
                input("\nInsufficient payment...")
                menu()

            elif Customer_Money > (Costs + Delivery_Cost):
                print("Thank you for purchasing at McFricky!\n"
                      "Have a good day!")

            else:
                invalid_input()
                cart_menu()

        elif y == "2":
            Costs = 0
            Items = 0
            List = []
            separator_line()
            input("My Cart has been reset... Press any key to continue...")
            cart_menu()

        elif y == "3":
            menu()

        else:
            invalid_input()
            cart_menu()

    else:
        input("There's currently nothing to purchase or reset in you Cart...\n"
              "Press any key to continue...")
        menu()


def invalid_input():
    separator_line()
    input("Invalid input... Press any key to continue...")


def separator_line():
    print("----------------------------------------------------------")

# ----------------------------------------------------------------------
'''Sequence'''

intro()
