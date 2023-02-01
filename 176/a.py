import math
n, x, t = map(int, input().split())

y = math.ceil(n / x) * t
print(int(y))
