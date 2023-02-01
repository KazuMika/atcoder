import math
a, b, h, m = map(int, input().split())
s_radius = m * 6
m_radius = h * 30 + 30 * (m/60)
a_radius = abs(s_radius - m_radius)
ans = math.sqrt(a**2+b**2 - 2*a*b*math.cos(math.radians(a_radius)))
print(ans)
