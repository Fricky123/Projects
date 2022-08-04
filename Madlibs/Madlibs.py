import random

num1 = 0
num2 = 1000
x = random.randint(num1, num2)
print(x)
answer = input("h,l,c: ")
if answer == "h":
    num2 -= (num2 - x)
    print(num2)
print(x)


# machine gives off a number(x)
# if high, number will not generate number <= x
# if low, number will not generate number >= x
# machine generates another number with those arguments
