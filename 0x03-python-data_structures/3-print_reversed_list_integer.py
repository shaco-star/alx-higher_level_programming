#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if not my_list:
        pass
    else:
        rev_list = my_list[::-1]
        for x in rev_list:
            print("{:d}".format(x))
