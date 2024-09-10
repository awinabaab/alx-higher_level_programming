#!/usr/bin/python3
def uppercase(str):
    for index in range(0, len(str)):
        char = str[index]
        print("{}".format(chr(ord(char) - 32)) if 96 < ord(str[index]) < 123
              else "{}".format(char), end='')
    print('\n', end='')
