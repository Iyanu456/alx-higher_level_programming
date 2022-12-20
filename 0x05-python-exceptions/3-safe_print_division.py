#!/usr/bin/python3
def safe_print_division(a, b):
    quo = 0
    try:
        quo = a / b
    except (ZeroDivisionError, ValueError, OverflowError):
        quo = none
    finally:
        print("Inside result: {}".format(quo))
        return quo
