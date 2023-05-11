#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    num_args = len(args)
    if num_args == 0:
        print("0 arguments.")
    elif num_args == 1:
        print("1 argument:")
        for i, arg in enumerate(args):
            print("{}: {}".format(i + 1, arg))
    else:
        print("Number of arguments: {}".format(num_args))
        for i, arg in enumerate(args):
            print("{}: {}".format(i + 1, arg))
