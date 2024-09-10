#!/usr/bin/python3
def uppercase(str):
    for char in str:
        print(f"{(ord(char) - 32 if 96 < ord(char) < 123 else ord(char)):c}",
              end='')
    print('\n', end='')
