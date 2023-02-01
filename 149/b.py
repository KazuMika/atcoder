a, b, k = map(int, input().split())

if a < k:
    k -= a
    a = 0
else:
    a -= k
    k = 0

b = max(0, b-k)
print(a, b)
