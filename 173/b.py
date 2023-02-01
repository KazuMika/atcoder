n = int(input())
ss = []
t = ['AC', 'WA', 'TLE', 'RE']
ans = [0, 0, 0, 0]
for i in range(n):
    ss.append(input())

for s in ss:
    if s == t[0]:
        ans[0] += 1
    elif s == t[1]:
        ans[1] += 1
    elif s == t[2]:
        ans[2] += 1
    elif s == t[3]:
        ans[3] += 1


for j, c in zip(t, ans):
    print(j, " x ", c)
