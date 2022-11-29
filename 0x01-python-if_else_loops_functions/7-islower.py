#!/usr/bin/python3
def islower(c):
    for i in c:
        if ord(i) in range(97,123):
            print("{} is lower".format(i))
        else:
            print("{} is upper".format(i))
