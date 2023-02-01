# -*- coding: utf-8 -*-

import numpy as np

def find_target():
    s = np.random.permutation(np.array(range(1, 10000)))
    target = 5000
    d = {}
    for i in s:
        d[target-i] = i

    for i in s:
        if i in d:
            print(d[i], i)

def money_find(target=22323873):
    d = {m: 0 for m in [10000, 1000, 500, 100, 50, 10, 5, 1]}

    for k in d.keys():
        while target >= k:
            d[k] += 1
            target -= k
    print(d)


def match():
    mens = [[2, 4, 5], [5, 1, 3], [6, 2, 3]]
    def dsf(inp):
