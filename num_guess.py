#!/usr/bin/env python3

# Created by: Mignonne Gihozo
# Created on: Oct 2026
# This program checks if a user's guess matches the correct answer.

import constants


def main():
    # input
    user_number = int(input("Enter a number: "))
    print("")

    # process & output
    if user_number == constants.CA:
        print("you are correct")
    else:
        print("you are not correct")


if __name__ == "__main__":
    main()
