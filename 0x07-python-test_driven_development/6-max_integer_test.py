#!/usr/bin/python3

def max_integer(list=[]):
    
    j = list[0]
    
    for i in list:
        if i >= j:
            j = i
    
    return j

list = [1, 34, 6, 2, 8, -89, 23, -54]
print(list)
print(max_integer(list))

