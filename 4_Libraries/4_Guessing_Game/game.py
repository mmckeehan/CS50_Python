# Create game.py
# Ask for LEVEL, player must INPUT positive whole number
# Generate random NUMBER between 1 and LEVEL
# Player will INPUT a GUESS
# If GUESS < NUMBER, PRINT "Too small!" Player will GUESS again
# If GUESS > NUMBER, PRINT "Too large!" Player will guess again
# If GUESS == NUMBER, PRINT "Just right!" and EXIT

import random
import sys


def main():
    level_select = user_level_selection()
    print(level_select)
    guess(level_select)


def user_level_selection():
    ls_bool = True

    while ls_bool == True:
        uls = input("Level: ")
        try:
            uls = int(uls)
            if uls > 0:
                ls_bool = False
        except ValueError:
            None
    if uls == 1:
        return 1
    else:
        return random.randrange(0, uls)


def guess(num):
    while True:
        u_guess = input("Guess a number: ")
        try:
            u_guess = int(u_guess)
            determination(u_guess, num)
        except ValueError:
            None


def determination(user_guess, number):
    if user_guess == number:
        print("Just right!")
        sys.exit()
    else:
        if user_guess < number:
            print("Too small!")
            guess(number)
        elif user_guess > number:
            print("Too large!")
            guess(number)


if __name__ == "__main__":
    main()
