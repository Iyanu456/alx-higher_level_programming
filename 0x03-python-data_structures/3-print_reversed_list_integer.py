#!/usr/bin/python3
def print_list_integer(my_list=[]):
    my_list.reverse()
    for integers in my_list:
        print("{:d}".format(integers))
        my_list.reverse()
