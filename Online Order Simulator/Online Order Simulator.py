import random
import locale
locale.setlocale(locale.LC_ALL, '')
# ----------------------------------------------------------------------

"""Online Order Simulator"""

# ----------------------------------------------------------------------
'''Data Values'''

# Cart
costs = 0
items = 0
List = ""
Balance = random.randint(50000, 100000)

# Food
f = {1: "Adobo",
     2: "Sinigang",
     3: "Pakbet",
     4: "Kinilaw",
     5: "Bulalo",
     6: "Chickenjoy sa Mcdo"}

# Prices for Food
f_p = {1: 50,
       2: 60,
       3: 334345,
       4: 234,
       5: 133,
       6: 1}

# Drinks
d = {1: "Coka-Cola (1 liter)",
     2: "Sprite (1 liter)",
     3: "Royal (1 liter)",
     4: "Water"}

# Prices for Drinks
d_p = {1: 50,
       2: 50,
       3: 50,
       4: 15}

# Miscellaneous
Delivery_Cost = 9999

# ----------------------------------------------------------------------
'''Main Functions (in order)'''

def intro():
    """Introductory script"""
    separator_line()
    # print("                 [MCFRICKY FOOD MACHINE]\n\n")
    page_title("MCFRICKY FOOD MACHINE")
    print("\nWelcome to McFricky!\n")

    x = (input("Would you like to order[y/n]? "))
    x.lower()

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
    page_title("MAIN MENU")
    customer_cart()

    if items:
        print("\n[1]Food Menu [2]Purchase/Reset Cart [e] Exit")
    else:
        print("[1]Food Menu [e] Exit")

    x = input("Choose option: ")

    if x == "1":
        food_menu()

    elif x == "2":
        if items:
            purchase_or_reset_cart()
        else:
            invalid_input()
            menu()

    elif x.lower() == "e":
        separator_line()
        y = input("Exit to Introductory page[y/n]: ")
        y.lower()

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

def purchase_or_reset_cart():
    global costs
    global items
    global List

    separator_line()

    page_title("PURCHASE/RESET CART MENU")

    if items:
        print(f"Cart = {costs:n} php\n"
              f"Delivery = {Delivery_Cost:n} pnp\n"
              f"Total Cost = {costs + Delivery_Cost:n} php\n\n"
              f"Your balance = {Balance:n} php - {costs + Delivery_Cost:n} php")

        if (Balance - (costs + Delivery_Cost)) < 0:
            print(f"You new balance = 0 php\n\n"
                  f"Insufficient payment, [Purchase] option will not be available...\n\n"
                  f"[1]Reset [e]Exit")
        else:
            print(f"You new balance = {(Balance - (costs + Delivery_Cost)):n} php\n\n"
                  f"[1]Reset [2]Purchase [e]Exit")

        y = input("Choose option: ")
        y.lower()

        if y == "1":
            separator_line()
            input("My Cart has been reset... Press any key to continue...")
            menu()

        elif y == "2":
            if Balance < (costs + Delivery_Cost):
                invalid_input()
                menu()

            elif Balance > (costs + Delivery_Cost):
                separator_line()
                print("Thank you for purchasing at McFricky!\n"
                      "Have a good day!")

            else:
                invalid_input()
                purchase_or_reset_cart()

        elif y == "e":
            menu()

        else:
            invalid_input()
            purchase_or_reset_cart()

    else:
        invalid_input()
        purchase_or_reset_cart()

def food_menu():
    """Provides customer with a list of choices for food"""

    separator_line()
    page_title("FOOD MENU")
    menu_database()

    x = input("\nChoose option: ")
    x.lower()

    if x == "e":
        print("(Exiting Food Menu...)")
        menu()

    elif x != "e" and (f.get(int(x))) is not None:
        transaction((int(x)))

    else:
        invalid_input()
        food_menu()

def transaction(x):
    """Make changes to COSTS/ITEMS/LIST in customer's CART based on his order"""
    separator_line()

    global costs
    global items
    global List

    page_title("TRANSACTION")

    print(f"\n{f.get(x)} selected...\n")

    try:
        quantity = int(input("Input quantity: "))

        if quantity > 1:
            print(f"\nYou are about to add {quantity} orders of {f.get(x)} to you Cart...\n")
        else:
            print(f"\nYou are about to add {quantity} order of {f.get(x)} to you Cart...\n")

        y = input("Add to cart[y/n]?: ")
        y.lower()

        if y == "y":
            costs += quantity * f_p.get(x)
            items += quantity
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
'''Utility Functions (To prevent repeating lines of code)'''

def customer_cart():
    if not List and not items:
        f'{Balance:n}'
        print("Your Cart:\n\n"
              f"Cost: ---\n"
              f"Items: ---\n"
              f"List: ---\n\n"
              f"Your balance: {Balance:n} php\n")

    else:
        print("Your Cart:\n\n"
              f"Cost: {costs:n} php\n"
              f"Items: {items}\n"
              f"List: {List}\n\n"
              f"Your balance: {Balance:n} php")

def invalid_input():
    separator_line()
    input("Invalid input... Press any key to continue...")

def separator_line():
    print("-----------------------------------------------------------")

def page_title(x):
    list(x)
    title = f""
    spaces = 57
    for _ in x:
        spaces -= 1
    title += (" " * int(spaces/2))
    title += f"[{x}]"
    print(title)

def menu_database():
    x = 1
    y = 1
    print(f"Meals:\n")
    for _ in f:
        print(f"[{x}]{f.get(x)} = {f_p.get(x):n} php")
        x += 1
    print(f"\nDrinks:\n")
    for _ in d:
        print(f"[{y}]{d.get(y)} = {d_p.get(y):n} php")
        y += 1


# ----------------------------------------------------------------------
'''Sequence'''

intro()
# ww----------------------------------------------------------------------
# made by me :)
# Pending changes:
#
