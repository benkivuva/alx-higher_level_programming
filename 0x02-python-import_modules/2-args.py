#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    total_sum = 0
    arguments = sys.argv[1:]  # Exclude the script name

    if len(arguments) == 0:
        print("0 arguments.")
    elif len(arguments) == 1:
        print("1 argument:")
        print("1:", arguments[0])
    else:
        print(f"{len(arguments)} arguments:")
        for index, argument in enumerate(arguments, start=1):
            print(f"{index}: {argument}")
