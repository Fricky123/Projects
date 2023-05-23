import random
import string


def password_generator(length):


    def letter_generator():
        random_lowercase_letter = random.choice(string.ascii_lowercase)
        randomUppercaseLetter = random.choice(string.ascii_uppercase)
        
        
        randomNumber = str(random.randint(1, 9))

        randomStuff = random.choice(["~", "!", "@", "#", "$", '%', '^', '&', '*'])


        generate = random.choice([randomStuff, randomNumber, randomUppercaseLetter, random_lowercase_letter])

        return generate

    password = ""

    letters = 0

    while letters != length:

        password += letter_generator()

        letters += 1


    return print("\nYour password: "+ password)


print("------Password Generator------\n")

try:

    length = int(input("Password length = "))

except ValueError:
    print('error')

    exit()
password_generator(length)

