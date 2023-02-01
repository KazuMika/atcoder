n = int(input())
s = [input() for _ in range(n)]
d = {}

for i in s:
    d[i] = d.get(i, 0) + 1


d = sorted(d.items(), key=lambda x: x[1], reverse=True)
maxv = d[0][1]
ans = []
for s in d:
    if s[1] == maxv:
        ans.append(s[0])
    else:
        break

for p in sorted(ans):
    print(p)
