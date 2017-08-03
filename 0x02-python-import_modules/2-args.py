#!/usr/bin/python3

from sys import argv


def main():

# new list - copies argv withing 1st argument(command)
    args_list = argv[1:]

    args = len(args_list)

    if args == 0:
        print("0 argument.")

    elif args == 1:
        print("1 argument:")

    else:
        print("{:d} arguments:".format(args))

    idx = 1
    for i in args_list:
        print("{}: {}".format(idx, args_list[idx - 1]))
        idx += 1


if __name__ == "__main__":
    main()
