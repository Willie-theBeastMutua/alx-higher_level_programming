#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if isinstance(my_list, list):
        leng = len(my_list) - 1
        copy_list = my_list
        if idx < 0 or idx > leng:
            return copy_list
        else:
            copy_list[idx] = element
            return copy_list
