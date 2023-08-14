#!/usr/bin/python3
increm = 1
for i in range(9):
    for j in range(increm, 10):
        if i < 8 or j < 9:
            print("{}{}, ".format(i, j), end="")
        else:
            print("{}{}".format(i, j))
    increm = increm + 1
