#!/usr/bin/python3
letters = "abcdefghijklmnopqrstuvwxyz"
for i in range(26):
    if letters[i] != "q" and letters[i] != "e":
        print("{}".format(letters[i]), end="")
    