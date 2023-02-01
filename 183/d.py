# -*- coding: utf-8 -*-
import numpy as np
n, w = map(int, input().split())
s = []
maxv = 0
for i in range(n):
    temp = list(map(int, input().split()))
    s.append(temp)
    maxv = max(maxv, temp[1])


cap = [0] * (maxv+1)
cap = np.array(cap)
for i in s:
    cap[i[0]:i[1]] += i[2]

for i in cap:
    if i > w:
        print('No')
        exit(0)

print('Yes')
