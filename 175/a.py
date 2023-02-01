# -*- coding: utf-8 -*-
s = input()

maxs = 0
ans = []
for a in s:
    if a == 'R':
        maxs += 1
    else:
        ans.append(maxs)
        maxs = 0


ans.append(maxs)
print(max(ans))
