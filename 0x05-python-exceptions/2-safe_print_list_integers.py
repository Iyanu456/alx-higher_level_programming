#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    limit = x
    index = 0
    count = 0
    while True:
        try:
            if index < limit:
                print("{:d}".format(my_list[index]), end="")
                index += 1
                count += 1
            else:
                print()
                return count
        except (ValueError, TypeError):
            try:
                index += 1
                limit += 1
                pass
            except IndexError:
                return count
    return count
