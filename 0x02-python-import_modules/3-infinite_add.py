#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":

    def infiniteadd():
        count = len(argv)-1
        sum = 0
        for i in range(1, count + 1):
            sum = sum + (int(argv[i]))
        print("{}".format(sum))
infiniteadd()
