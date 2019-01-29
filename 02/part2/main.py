#!/usr/bin/env python3

import os, sys

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()

    checksum = 0
    for line in lines:
        vals = [int(x) for x in line.split()]
        for x in range(len(vals)):
            for y in range(x+1,len(vals)):
                # print(vals[x], vals[y])
                if vals[x] % vals[y] == 0:
                    checksum += vals[x] // vals[y]
                    # print(vals[x], vals[y], vals[x] // vals[y])
                elif vals[y] % vals[x] == 0:
                    checksum += vals[y] // vals[x]
                    # print(vals[x], vals[y], vals[y] // vals[x])

    print(checksum)
