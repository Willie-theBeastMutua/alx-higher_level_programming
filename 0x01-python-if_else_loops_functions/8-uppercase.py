#!/usr/bin/python3
def uppercase(str):
    for i in str:
        num = ord(i)
        if num > 96 and num < 123:
            num = num - 32
        print("%c"% num, end="")
    print()
