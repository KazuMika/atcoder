n = int(input())
x = list(map(int, input().split()))

mid = sum(x)//len(x)

ans = float('inf')
for i in [-1, 0, 1]:
    temp = sum([(i+j-mid)**2 for j in x])
    ans = min(temp, ans)
print(ans)
