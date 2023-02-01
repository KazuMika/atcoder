from collections import defaultdict as dic
n, m = map(int, input().split())
ac = 0
pena = 0
d = dic(list)
for i in range(m):
    pi, si = input().split()
    d[pi].append(si)

for (k, v) in d.items():
    pe = 0
    flag = False
    for aw in v:
        if aw == 'WA':
            pe += 1
        else:
            ac += 1
            pena += pe
            break

print(ac, pena)
