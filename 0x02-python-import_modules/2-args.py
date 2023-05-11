#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    total_sum = 0

    num_arguments = len(sys.argv) - 1
    argument_string = "argument" if num_arguments == 1 else "arguments"
    print(f"Number of {argument_string}: {num_arguments}")

    for index, value in enumerate(sys.argv[1:], start=1):
        print(f"{index}: {value}")
        try:
            argument = int(value)
            total_sum += argument
        except ValueError:
            pass

    print("Total sum:", total_sum)
