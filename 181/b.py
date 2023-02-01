n = int(input())
ans = 0
for i in range(n):
    a, b = map(int, input().split())
    ans += int((b*(b+1))/2 - ((a-1)*(a))/2)


print(ans)
