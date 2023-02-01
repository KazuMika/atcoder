n = int(input())
ans = 0
mod = 10**9 + 7
ans += 10**n % mod
ans -= 9**n % mod
ans -= 9**n % mod
ans += 8**n % mod

print(ans)
