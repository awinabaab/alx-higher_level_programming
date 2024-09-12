#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    names = dir(hidden_4)
    for index in range(0, len(names)):
        if names[index].startswith('__'):
            continue
        print(names[index])
