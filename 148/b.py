n = int(input())
s, t = input().split()
ans = ''
for x, y in zip(s, t):
    ans += x + y

print(ans)
