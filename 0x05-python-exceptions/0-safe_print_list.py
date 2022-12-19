#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    for i in range (x):
        elements = 0
        try:
            print("{}".format(my_list[i]), end="")
            elements += 1
        except:
            pass
    print()
    return elements
my_list = [1, 2, 3,  4, 5]
safe_print_list(my_list, 3)

