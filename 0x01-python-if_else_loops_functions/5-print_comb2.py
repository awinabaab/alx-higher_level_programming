#!/usr/bin/python3
for ncomb in range(0, 100):
    print("{:02d}".format(ncomb), end=', ' if ncomb < 99 else '\n')
