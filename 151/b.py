n, k, m = map(int, input().split())
a = list(map(int, input().split()))
suma = sum(a)
x = (m*n) - (suma)
x = max(x, 0)

if x > k:
    print(-1)
else:
    print(x)
