#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    total = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            total += 1
        except (IndexError, TypeError, ValueError):
            pass
    print()
    return total
