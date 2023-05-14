#!/usr/bin/python3

def element_at(my_list, idx, element):
    if idx > (len(my_list) - 1) or idx < 0:
        return my_list
    return my_list[idx] = element
