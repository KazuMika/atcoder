import math
n = int(input())
i = 1
ans = n

limit = math.sqrt(n)

while i <= limit:
    if n % i == 0:
        div = n // i
        ans = min(ans, div+i-2)

    i += 1

print(ans)
