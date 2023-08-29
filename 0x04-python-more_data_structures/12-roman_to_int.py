#!/usr/bin/python3

def roman_to_int(roman_string):
    if type(roman_string) == str or roman_string:
        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        sum = 0
        prev = 0
        for i in roman_string[::-1]:
            for k, v in dic.items():
                if i == k:
                    if v >= prev:
                        sum += v
                    else:
                        sum -= v
                    prev = v
    else:
        return 0
    return sum
