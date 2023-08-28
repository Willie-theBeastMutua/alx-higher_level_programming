#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    leng = len(my_list) - 1
    while 0 <= leng:
        print("{:d}".format(my_list[leng]))
        leng -= 1
