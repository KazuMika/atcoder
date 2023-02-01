# -*- coding: utf-8 -*-
k = int(input())
ans = 0
n = 7

if k % 2 == 0 or k % 5 == 0:
    print(-1)
    exit(0)
c = 1
while True:
    if n % k == 0:
        break
    n = (n * 10 + 7) % k
    c += 1

print(c)
