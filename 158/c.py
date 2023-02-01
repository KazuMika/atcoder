a, b = map(int, input().split())

x = a // 0.08
y = b // 0.10
x, y = int(x), int(y)
minv = min(x, y)
maxv = max(x, y)
ans = []

for i in range(minv, maxv+2):
    if int(i * 0.08) == a and int(i * 0.1) == b:
        ans.append(i)

if len(ans) == 0:
    print(-1)
else:
    print(min(ans))
