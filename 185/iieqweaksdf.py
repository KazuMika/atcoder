# -*- coding: utf-8 -*-
n = 10
c = 0
for i in range(n):
    for j in range(n):
        if i != j:
            c += 1
print(c)
ans = 1
for i in range(1, n+1):
    ans *= i
print(ans)
