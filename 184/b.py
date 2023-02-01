n, x = map(int, input().split())
s = input()
ans = x
for i in s:
    temp = 1 if i == 'o' else -1
    ans = max(0, ans+temp)

print(ans)
