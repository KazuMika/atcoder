# -*- coding: utf-8 -*-
n = int(input())
a = list(map(int, input().split()))


d = {}
for num in a:
    d[num] = d.get(num, 0) + 1


for i in range(1, len(a)+2):
    if i in d:
        print(d[i])
    else:
        print(0)
