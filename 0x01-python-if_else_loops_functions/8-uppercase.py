#!/usr/bin/python3
def uppercase(s):
    for c in s:
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            upper_c = chr(ord(c) - 32)
            print("{}".format(upper_c), end="")
        else:
            print("{}".format(c), end="")
    print()
