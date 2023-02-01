# -*- coding: utf-8 -*-
x, n = map(int, input().split())
ps = list(map(int, input().split()))

for i in range(0, x+100):
    for j in [-1, 1]:
        temp = x + (i*j)
        if ps.count(temp) == 0:
            ans = temp
            break
    else:
        continue
    break


print(ans)
