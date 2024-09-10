#!/usr/bin/python3
for ncomb in range(1, 100):
    if (ncomb // 10 > ncomb % 10) or (ncomb // 10 == ncomb % 10):
        continue
    else:
        print("{:02d}".format(ncomb), end=', ' if ncomb < 89 else '\n')
