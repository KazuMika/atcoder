h, w = map(int, input().split())
a = []
minv = float('inf')
for i in range(h):
    a.append(list(map(int, input().split())))
    minv = min(minv, min(a[i]))

ans = 0
for i in range(len(a)):
    for j in range(len(a[0])):
        ans += a[i][j]-minv
print(ans)
