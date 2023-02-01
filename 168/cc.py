import math
a, b, h, m = map(int, input().split())
h = h * 30 + (30*m/60)
m = m * 6
radius = abs(m-h)
ans = math.sqrt(b**2+a**2-2*a*b*math.cos(math.radians(radius)))
print(ans)
