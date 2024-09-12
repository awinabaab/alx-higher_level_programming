#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv_len = len(sys.argv)
    arg_num = argv_len - 1
    print("{:d} {}{}".format(arg_num,
          "arguments" if (arg_num > 1 or arg_num == 0) else "argument",
          ':' if (arg_num >= 1) else '.'))
    for argc in range(1, argv_len):
        print("{:d}: ".format(argc), "{}".format(sys.argv[argc]))
