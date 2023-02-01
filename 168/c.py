import math
import numpy
a, b, h, m = map(int, input().split())
ji = 30 * h
hun = 6 * m
dif = abs(ji-hun) + 20
x = a**2 + b**2 - (2*a*b * math.cos(math.radians(dif)))
print(x)
x = numpy.sqrt(x)
print(x)
