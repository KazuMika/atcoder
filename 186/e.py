from math import gcd
def lcm(x, y):
    return (x * y) // gcd(x, y)


t = int(input())

test = []

for i in range(t):
    test.append(map(int, input().split()))

for (n, s, k) in test:
    if (n-s) % k == 0:
        print((n-s)//k)
    else:
