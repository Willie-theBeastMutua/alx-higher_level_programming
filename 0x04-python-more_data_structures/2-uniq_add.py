#!/usr/bin/python3

def uniq_add(my_list=[]):
    # leng = len(my_list)
    j = 0
    val = 0
    while j < len(my_list):
        idx = my_list.index(my_list[j])
        if idx < j:
            j += 1
            continue
        else:
            val += my_list[j]
        j += 1
    return val
