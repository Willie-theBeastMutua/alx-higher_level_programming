#!/usr/bin/python3
def uppercase(str):
    result = ""
    for i in str:
        num = ord(i)
        if num > 96 and num < 123:
            num = num - 32
        print("%c"% num, end="")
    print("")
#!/usr/bin/python3


def upper(ch):
    new = ord(ch)
    if new > 96 and new < 123:
        return new - 32
    else:
        return new


def uppercase(str):
    empty = ""
    for i in range(len(str)):
        empty += "%c" % upper(str[i])
    print("{:s}".format(empty))
