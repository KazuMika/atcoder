n, k = map(int, input().split())
s = [int(input()) for i in range(n)]

if 0 in s:
    print(len(s))
    exit(0)

r, ans, temp = 0, 0, 1
for l in range(n):
    while r < n and temp*s[r] <= k:
        temp *= s[r]
        r += 1

    ans = max(ans, r-l)
    if r == l:
        r += 1
    else:
        temp //= s[l]

print(ans)
