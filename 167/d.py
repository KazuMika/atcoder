n, k = map(int, input().split())
a = list(map(int, input().split()))

now = a[0]
if k % n == 0:
    k = n
else:
    k = k % n + n

for i in range(k):
    now = a[now-1]

print(now)
