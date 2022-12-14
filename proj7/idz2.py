#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

if __name__ == '__main__':
    a = list(map(float, input("Input list: ").split()))
    a1 = []
    min_a = a[0]
    min_i = 0
    s = 0

    for i in range(0, len(a)):
        if a[i] < min_a:
            min_a = a[i]
            min_i = i

    for i in range(0, len(a)):
        if a[i] < 0:
            a1.append(i)

    w1 = a1[0]
    w2 = a1[1]

    for i in a[a1[0] + 1: a1[1]]:
        s += i

    a.sort(key=abs)

    print(' '.join(map(str, a)))
    print("Index of min elem:", min_i, "\n", "Sum elem:", s)