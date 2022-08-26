import random
import locale
locale.setlocale(locale.LC_ALL, '')
# ----------------------------------------------------------------------
"""Order Simulator"""
# ----------------------------------------------------------------------
'''Variables'''

# Cart
costs = 0
items = 0
List = None
balance = random.randint(50000, 100000)

# Meals
m = {1: "Adobo",
     2: "Sinigang",
     3: "Pakbet",
     4: "Kinilaw",
     5: "Bulalo",
     6: "Chickenjoy sa Mcdo"}

# Prices for Meals
m_p = {1: 50,
       2: 60,
       3: 334345,
       4: 234,
       5: 133,
       6: 1}

# Drinks
d = {1: "Coka-Cola Litro",
     2: "Sprite Litro",
     3: "Royal Litro",
     4: "Water"}

# Prices for Drinks
d_p = {1: 50,
       2: 50,
       3: 50,
       4: 15}

# Miscellaneous
delivery_cost = 9999


# ----------------------------------------------------------------------
'''Main Functions (in order)'''


def intro():
    """Introductory script"""
    separator_line()
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
    """Provides customer with a menu"""
    separator_line()
    page_title("MAIN MENU")
    customer_cart()

    if items:
        print("\n[1]Meals [2]Drinks [3]Purchase/Reset Cart [e] Exit")
    else:
        print("[1]Meals [2]Drinks [e] Exit")

    x = input("Choose option: ")

    if x == "1":
        print("Meals:\n")
        food_or_drinks_menu(m, m_p)

    elif x == "2":
        print("Drinks:\n")
        food_or_drinks_menu(d, d_p)

    elif x == "3":
        if items:
            purchase_or_reset_cart()
        else:
            invalid_input()
            menu()

    elif x.lower() == "e":
        separator_line()
        y = input("Are you sure you want to exit[y/n]: ")
        y.lower()

        if y == "y":
            separator_line()
            print("Goodbye!")

        elif y == "n":
            menu()

        else:
            invalid_input()
            menu()

    else:
        invalid_input()
        menu()

def food_or_drinks_menu(foodtype, foodtype_price):
    """Provides customer with a menu for food"""
    separator_line()
    if foodtype == m:
        page_title("MEALS")
    else:
        page_title("DRINKS")

    print("Choose one at a time:")

    x = 1
    for _ in foodtype:
        print(f"[{x}]{foodtype.get(x)} = {foodtype_price.get(x):n} php")
        x += 1

    choice = input("[e]Exit"
                   "\nChoose option: ")

    if choice == "e":
        print("(Exiting Food Menu...)")
        menu()

    elif foodtype.get(int(choice)) is not None:
        transaction(foodtype, foodtype_price, int(choice))

    else:
        invalid_input()
        food_or_drinks_menu(foodtype, foodtype_price)

def purchase_or_reset_cart():
    global costs
    global items
    global List

    separator_line()

    page_title("PURCHASE/RESET CART MENU")

    if items:
        print(f"\nTotal Cost = Your Cart + Delivery Cost\n"
              f"Total Cost = {costs:n} php + {delivery_cost:n} php\n"
              f"Total Cost = {costs + delivery_cost:n} php\n"
              f"Your balance: {balance:n} php\n\n"
              f"Your new balance: {balance - (costs + delivery_cost):n}")

        if (balance - (costs + delivery_cost)) < 0:
            print(f"Insufficient payment...\n\n"
                  f"[1]Reset [e]Exit")
        else:
            print(f"[1]Reset [2]Purchase [e]Exit")

        y = input("Choose option: ")
        y.lower()

        if y == "1":
            costs = 0
            items = 0
            List = ""
            separator_line()
            input("Your Cart has been reset... Press any key to continue...")
            menu()

        elif y == "2":
            if balance < (costs + delivery_cost):
                invalid_input()
                menu()

            elif balance > (costs + delivery_cost):
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

def transaction(foodtype, foodtype_price, choice):
    """Make changes to COSTS/ITEMS/LIST in customer's cart"""
    separator_line()

    global costs
    global items
    global List

    page_title("TRANSACTION")

    print(f"{foodtype.get(choice)} selected...")

    quantity = int(input("Input quantity: "))

    if quantity > 1:
        print(f"You are about to add {quantity} orders of {foodtype.get(choice)} to you Cart...")
    else:
        print(f"You are about to add {quantity} order of {foodtype.get(choice)} to you Cart...")

    y = input("Add to cart[y/n]?: ")
    y.lower()

    if y == "y":
        costs += quantity * foodtype_price.get(choice)
        items += quantity
        if not List:
            List = f"{foodtype.get(choice)}({quantity:n})"
        else:
            List += f", {foodtype.get(choice)}({quantity:n})"
        separator_line()
        print(f"{quantity} order/s of {foodtype.get(choice)} added to Cart...")

        menu()

    elif y == "n":
        separator_line()
        print("\nOrder cancelled...\n")
        food_or_drinks_menu(foodtype, foodtype_price)

    else:
        invalid_input()
        food_or_drinks_menu(foodtype, foodtype_price)


# ----------------------------------------------------------------------
'''Utility Functions (To prevent repeating lines of code)'''


def customer_cart():
    if not List and not items:
        f'{balance:n}'
        print("Your Cart:\n\n"
              f"Items: ---\n"
              f"List: ---\n"
              f"Cost: ---\n"
              f"Your balance: {balance:n} php\n")

    else:
        print("Your Cart:\n\n"
              f"Items: {items:n}\n"
              f"List: {List}\n"
              f"Cost: {costs:n} php\n"
              f"Your balance: {balance:n} php")

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

# ----------------------------------------------------------------------
'''Sequence'''

intro()
# ww----------------------------------------------------------------------
# made by me :)
