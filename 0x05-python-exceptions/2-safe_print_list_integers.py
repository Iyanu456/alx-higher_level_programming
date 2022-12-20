#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    index = 0
    while index < x:
        try:
            print("{:d}".format(my_list[index]), end="")
            index += 1
        except (ValueError, TypeError, IndexError):
            pass
    print()
    return index
list =[1, 2, 3, "School", "Iyanu", 5, 6]
count = safe_print_list_integers(list, 5)
print("{}".format(count))
