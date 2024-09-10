#!/usr/bin/python3
for char in range(ord('z'), ord('a') - 1, -1):
    print((f"{char:c}") if (char % 2 == 0) else (f"{(char - 32):c}"), end='')
