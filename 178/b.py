a, b, c, d = map(int, input().split())
x1 = a * c
x2 = a * d
x3 = b * d
x4 = b * c
m = max(x1, x2, x3, x4)
print(m)
