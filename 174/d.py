# -*- coding: utf-8 -*-
n = int(input())
cs = input()
r_num = 0
w_num = 0
# RRR|WWWW にする
r_num = cs.count('R')
w_num = cs.count('W')

if r_num == 0 or w_num == 0:
    print(0)
else:
    ans = []
    W = 0
    rl_num = 0
    for c in cs:
        if c == 'R':
            rl_num += 1
        elif c == 'W':
            W += 1
        R = r_num - rl_num
        ans.append(max(W, R))

    print(min(ans))
