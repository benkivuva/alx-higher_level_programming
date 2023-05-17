#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        sum_s = sum(w * s for s, w in my_list)
        sum_w = sum(w for _, w in my_list)
        return sum_s / sum_w if sum_w != 0 else 0
    return 0
