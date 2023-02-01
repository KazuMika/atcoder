n = int(input())
ans = 0
for num in range(1, n+1):
    con1 = '7' in str(num)
    s = oct(num)[2:]
    con2 = '7' in s
    if not con1 and not con2:
        ans += 1

print(ans)
