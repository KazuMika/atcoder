# -*- coding: utf-8 -*-

n, m = map(int, input().split())
a = list(map(int, input().split()))

ans = n - sum(a)

if ans < 0:
    print(-1)
else:
    print(ans)
