#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    dic_cp = a_dictionary.copy()
    for k, v in dic_cp.items():
        v *= 2
        dic_cp[k] = v
    return dic_cp
