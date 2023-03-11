from collections import deque


def print_reversed_list_integer(my_list=[]):
    new_list = []
    for i in range(len(my_list)):
        my_list = deque(my_list)
        new_list.append(my_list.pop())
    for i in range(len(new_list)):
        print("{:d}".format(new_list[i]))