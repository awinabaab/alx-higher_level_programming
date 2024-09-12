#!/usr/bin/python3
import sys

if __name__ == "__main__":
    infinite_add = 0
    argv_len = len(sys.argv)
    for arg in range(1, argv_len):
        infinite_add += int(sys.argv[arg])
    print(infinite_add)
