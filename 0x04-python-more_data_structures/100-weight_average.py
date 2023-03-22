#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    total_sum = 0
    weight_sum = 0
    for item in my_list:
        total_sum += (item[0] * item[1])
        weight_sum += item[1]
    return (total_sum / weight_sum)
