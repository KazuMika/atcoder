# -*- coding: utf-8 -*-
from collections import Counter as C

h, w, m = map(int, input().split())

hs, ws = [], []
hw = []

for i in range(m):
    hi, w = map(int, input().split())
    hs.append(hi)
    ws.append(w)
    hw.append([hi, w])


ch = C(hs).most_common()
cw = C(ws).most_common()
anss = []
pre_ans = -float('inf')
mrow = ch[0][0]
mcow = cw[0][0]

for num1, num2 in zip(ch, cw):
    row, cow = num1[0], num2[0]
    ans = num1[1] + num2[1]
    if [row, cow] in hw:
        ans -= 1
    anss.append(ans)
    if (mrow > row or mcow > cow) and pre_ans > ans:
        break

    if pre_ans < ans:
        pre_ans = ans


print(max(anss))
