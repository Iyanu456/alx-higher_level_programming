#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    tmp = a_dictionary.copy()
    for keys in tmp.keys:
        tmp[keys] *= 2
    return (tmp)
