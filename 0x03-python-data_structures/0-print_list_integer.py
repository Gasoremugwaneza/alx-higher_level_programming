#!/usr/bin/python3
# a function that print integer from the list
def print_list_integer(my_list=[]):
    for i in range(0, len(my_list)):
        print("{:d}".format(my_list[i]))
