#!/usr/bin/python3

import sys
if __name__ == "__main__":
    total_sum = 0

    arguments = sys.argv[1:]
    for argument in arguments:
        total_sum += int(argument)
    print(total_sum)
