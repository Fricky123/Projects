import random
import locale
locale.setlocale(locale.LC_ALL, '')
# ----------------------------------------------------------------------

"""Online Order Simulator"""

# ----------------------------------------------------------------------
'''Global Variables'''

# Cart
Costs = 0
Items = 0
List = ""
Balance = random.randint(50000, 100000)

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

    if Items:
        print("\n[1]Food Menu [2]Purchase/Reset Cart [e] Exit")
    else:
        print("[1]Food Menu [e] Exit")

    x = input("Choose option: ")

    if x == "1":
        food_menu()

    elif x == "2":
        if Items:
            cart_menu()
        else:
            invalid_input()
            menu()

    elif x == "e":
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

def cart_menu():
    global Costs
    global Items
    global List

    separator_line()

    if Items:
        print(f"Cart = {Costs:n} php\n"
              f"Delivery = {Delivery_Cost:n} pnp\n"
              f"Total Cost = {Costs + Delivery_Cost:n} php\n\n"
              f"Your balance = {Balance:n} php - {Costs + Delivery_Cost:n} php")

        if (Balance - (Costs + Delivery_Cost)) < 0:
            print(f"You new balance = 0 php\n\n"
                  f"Insufficient payment, [Purchase] option will not be available...\n\n"
                  f"[1]Reset [e]Exit")
        else:
            print(f"You new balance = {(Balance - (Costs + Delivery_Cost)):n} php\n\n"
                  f"[1]Reset [2]Purchase [e]Exit")

        y = input("Choose option: ")

        if y == "1":
            separator_line()
            input("My Cart has been reset... Press any key to continue...")
            menu()

        elif y == "2":
            if Balance < (Costs + Delivery_Cost):
                invalid_input()
                menu()

            elif Balance > (Costs + Delivery_Cost):
                separator_line()
                print("Thank you for purchasing at McFricky!\n"
                      "Have a good day!")

            else:
                invalid_input()
                cart_menu()

        elif y == "e":
            menu()

        else:
            invalid_input()
            cart_menu()

    else:
        invalid_input()
        cart_menu()

def food_menu():
    """Provides customer with a list of choices for food"""

    separator_line()

    print(f"Food Menu:\n"
          f"[1]{f.get('f1')} = {f_p.get('f1'):n} php\n"
          f"[2]{f.get('f2')} = {f_p.get('f2'):n} php\n"
          f"[3]{f.get('f3')} = {f_p.get('f3'):n} php\n"
          f"[4]{f.get('f4')} = {f_p.get('f4'):n} php\n"
          f"[5]{f.get('f5')} = {f_p.get('f5'):n} php\n"
          f"[e]Exit\n")

    x = input("Choose option: ")

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
    elif x == "e":
        print("(Exiting Food Menu...)")
        menu()

    else:
        invalid_input()
        food_menu()

def transaction(x):
    """Make changes to COSTS/ITEMS/LIST in customer's CART based on his order"""
    separator_line()

    global Costs
    global Items
    global List

    print(f"{f.get(x)} selected...\n")

    try:
        quantity = int(input("Input quantity: "))

        if quantity > 1:
            print(f"\nYou are about to add {quantity} orders of {f.get(x)} to you Cart...\n")
        else:
            print(f"\nYou are about to add {quantity} order of {f.get(x)} to you Cart...\n")

        y = input("Add to cart[y/n]?: ")

        if y == "y":
            Costs += quantity * f_p.get(x)
            Items += quantity
            if not List:
                List += f"{f.get(x)}({(str(quantity))})"
            else:
                List += f", {f.get(x)}({(str(quantity))})"
            print(f"\n{quantity} order/s of {f.get(x)} added to Cart...")

            menu()

        elif y == "n":
            separator_line()
            print("\nOrder cancelled...\n")
            food_menu()

        else:
            invalid_input()
            food_menu()

    except ValueError:
        invalid_input()
        separator_line()
        food_menu()

# ----------------------------------------------------------------------
'''Utility Functions'''

def customer_cart():
    if not List and not Items:
        f'{Balance:n}'
        print("Your Cart:\n\n"
              f"Cost: ---\n"
              f"Items: ---\n"
              f"List: ---\n\n"
              f"Your balance: {Balance:n} php\n")

    else:
        print("Your Cart:\n\n"
              f"Cost: {Costs:n} php\n"
              f"Items: {Items}\n"
              f"List: {List}\n\n"
              f"Your balance: {Balance:n} php")

def invalid_input():
    separator_line()
    input("Invalid input... Press any key to continue...")

def separator_line():
    print("----------------------------------------------------------")

# ----------------------------------------------------------------------
'''Sequence'''

intro()
# ----------------------------------------------------------------------
