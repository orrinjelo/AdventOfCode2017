#!/usr/bin/env python3

import os, sys

if __name__ == '__main__':
    try:
        with open(sys.argv[1], 'r') as f:
            lines = f.readlines()
        line = lines[0]
        l = len(line)
    except:
        line = sys.argv[1]
        l = len(line)

    count = 0
    for i in range(l):
        if line[i] == line[(i+l//2)%l]:
            count += int(line[i])

    print(count)