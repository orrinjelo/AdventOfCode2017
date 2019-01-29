#!/usr/bin/env python3

import os, sys

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()

    checksum = 0
    for line in lines:
        vals = [int(x) for x in line.split()]
        checksum += max(vals) - min(vals)

    print(checksum)
