import random

y = int(input("I have selected a number between one and ten.  Guess what it is?"))
x = random.randint(1,10)

while x != y:
    if x != y:
        y = int(input("That is incorrect, please guess again. "))

print("that is correct! The answer is " + str(x) + "!")
