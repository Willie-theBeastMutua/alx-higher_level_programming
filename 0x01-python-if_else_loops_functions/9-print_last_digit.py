#!/usr/bin/python3

def print_last_digit(number):
    mult = 1
    if number < 0:
        mult = -1
        number = number * mult
    print("{}".format(number % 10), end="")
    return (number % 10)
