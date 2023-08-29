#!/usr/bin/python3

def best_score(a_dictionary):
    val = 0
    if isinstance (a_dictionary, dict):
        for k, v in a_dictionary.items():
            if v > val:
                val = v
                biggest = k
    else:
        return None
    return k
