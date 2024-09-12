#!/usr/bin/python3
def remove_char_at(str, n):
    string = str[0:n] + str[n+1:]
    return (str if n < 0 else string)
