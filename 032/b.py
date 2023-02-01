# -*- coding: utf-8 -*-
s = input()
k = int(input())
ans = set()
for i in range(len(s)-k+1):
    temp = s[i:i+k]
    ans.add(temp)

print(len(ans))
