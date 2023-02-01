n = int(input())
a = list(map(int, input().split()))
ans = 0
maxh = 0
for i in range(len(a)-1):
    if maxh < a[i]:
        maxh = a[i]
    if maxh > a[i+1]:
        ans += maxh - a[i+1]


print(ans)
