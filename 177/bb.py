# -*- coding: utf-8 -*-
s = input()
t = input()

ans = len(t)

for i in range(len(s)-len(t)+1):
    dif = 0
    for j in range(len(t)):
        if s[j+i] != t[j]:
            dif += 1

    ans = min(ans, dif)

print(ans)
