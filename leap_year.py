#!/usr/bin/env python3

# Created by Donggeun Lim
# Created on December 2020
# This program checks the year is leap year or no

import constants


def main():

    year_string = input("Enter your year: ")
    print("")

    try:
        year_number = int(year_string)
        divisible_four = year_number % constants.LEAP_YEAR_FOUR
        divisible_hundred = year_number % constants.LEAP_YEAR_HUNDRED
        divisible_four_hundred = year_number % constants.LEAP_YEAR_FOUR_HUNDRED

        if divisible_four == 0:
            if divisible_hundred == 0:
                if divisible_four_hundred == 0:
                    print("This year is a leap year")
                else:
                    print("This year is a not leap year")
            else:
                print("This year is a leap year")
        else:
            print("This year is a not leap year")

    except Exception:
        print("This was not an integer")


if __name__ == "__main__":
    main()
