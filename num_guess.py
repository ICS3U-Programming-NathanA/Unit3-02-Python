#!/usr/bin/env python3
# Created by: Nathan Araujo
# Created on: Oct 5 2022
# This program asks the user for a number between 0 and 9 and then sees if they got the same number as the computer


import constants


def main():

    # Get the the number they guessed
    user_num = int(input("Enter a number between 0 and 9: "))

    # An If statement to see if they got the same number as the secret number then display the results
    if constants.SECRET_NUM == user_num:
        print("You guessed the correct number")
    else:
        print("You guessed the wrong number")


if __name__ == "__main__":
    main()
