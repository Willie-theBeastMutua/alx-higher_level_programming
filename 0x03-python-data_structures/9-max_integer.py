#!/usr/bin/python3

def max_integer(my_list=[]):
    leng = len(my_list)
    if leng < 1:
        return None
    j = 0
    maxi = my_list[0]
    while j < leng - 1:
        if my_list[j] > maxi:
            maxi = my_list[j]
        j += 1
    return maxi
