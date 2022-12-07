#!/usr/bin
def search_replace(my_list, search, replace):
    return (list(map(lambda x: replace if x is search else x)))
