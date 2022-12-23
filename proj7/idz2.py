#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

if __name__ == '__main__':
    a = list(map(float, input("Input list: ").split()))
    a1 = []
    min_i = 0
    s = 0

    if not a:
        print(
            "заданный список пуст",
            file=sys.stderr
        )
        exit(1)

    min_a = a[0]

    for i, item in enumerate(a, 1):
        if item < min_a:
            min_a = item
            min_i = i

    for i, item in enumerate(a):
        if item < 0:
            a1.append(i)

    w1 = a1[0]
    w2 = a1[1]

    for i in a[a1[0] + 1: a1[1]]:
        s += i

    a.sort(key=abs)

    print(' '.join(map(str, a)))
    print("Num of min elem:", min_i, "\n", "Sum elem:", s)