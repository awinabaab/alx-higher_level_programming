#!/usr/bin/python3
for ncomb in range(1, 100):
    if (ncomb // 10 > ncomb % 10) or (ncomb // 10 == ncomb % 10):
        continue
    else:
        print(f"{ncomb:02d}", end=', ' if ncomb < 89 else '\n')
