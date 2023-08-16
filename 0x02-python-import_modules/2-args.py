#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    num = len(argv)-1
    if num == 0:
        print("{} arguments.".format(num))
    if num == 1:
        print("{} argument:".format(num))
    if num > 1:
        print("{} arguments:".format(num))
    count = 0
    for i in argv:
        if count > 0:
            print("{}: {}".format(count, i))
        count += 1
