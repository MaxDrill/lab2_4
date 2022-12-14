#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

if __name__ == '__main__':
    A = list(map(int, input().split()))
    if len(A) != 10:
        print("there are't 10 items in the list", file=sys.stderr)
        exit(1)
    p = 1
    for i in A:
        if i < 0:
            p *= i
    print(p)