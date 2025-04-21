# Using the random module the computer "thinks" about a whole number between 1 and 20.
# The user has to guess the number. After the user types in the guess the computer
# tells if this was bigger or smaller than the number it generated, or if it was the same.
# The game ends after just one guess.

import random

random20 = random.randrange(1,21)

inp_by_user = int(input("Welcome to the Number Guessing Game! your guess is: "))

if inp_by_user == random20 :
    print("We have a Winner! Your guess was correct!")
elif inp_by_user < random20:
    print("You missed! Your guess was too low!")
else:
    print("You missed! Your guess was too high!")