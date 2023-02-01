import math
a = int(input())
b = int(input())
n = int(input())
def lcm(x, y):
    return (x * y) // math.gcd(x, y)


g = lcm(a, b)
i = 1
while True:
    if g*i >= n:
        print(g*i)
        exit(0)
    else:
        i += 1
