import sys

if __name__ == "__main__":
    args = sys.argv[1:]  # Exclude the script name from the list

    num_args = len(args)
    plural_s = "s" if num_args > 1 else ""

    # Print the number of arguments
    print(f"Number of argument{plural_s}: {num_args}")

    # Print the list of arguments
    print("Argument{}:".format("s" if num_args > 0 else ""), end=" ")

    if num_args > 0:
        for i, arg in enumerate(args, start=1):
            print(f"{i}: {arg}")
    else:
        print(".")

