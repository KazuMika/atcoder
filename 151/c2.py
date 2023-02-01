# -*- coding: utf-8 -*-
n, m = map(int, input().split())
ck = set()
pe = 0
ac = 0
penalty = 0
cp = [0] * (n+1)
for i in range(m):
    p, s = input().split()
    p = int(p)
    if p in ck:
        continue

    if s == 'WA':
        cp[p] += 1
    else:
        penalty += cp[p]
        pe = 0
        ac += 1
        ck.add(p)

print(ac, penalty)
