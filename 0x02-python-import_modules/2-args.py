#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    total_sum = 0

    # Iterate over the command-line arguments
    for index, value in enumerate(sys.argv):
        # Skip the first argument, which is the script name itself
        if index == 0:
            continue

        # Convert the argument to an integer and add it to the sum
        argument = int(value)
        total_sum += argument

    # Print the final sum
    print("Total sum:", total_sum)
