n, k = map(int, input().split())
t = n % k
t1 = k-t
if t < t1:
    print(t)
else:
    print(t1)
