#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    weight = sum(score * x for score, x in my_list)
    total = sum(x for score, x in my_list)
    return weight / total
