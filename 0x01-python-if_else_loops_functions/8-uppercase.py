#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            letter = ord(i) - 32
        else:
            letter = ord(i)
        print("{:s}".format(chr(letter)), end="")
    print("")
