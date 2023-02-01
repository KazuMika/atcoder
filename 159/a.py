import math
n, m = map(int, input().split())

def comb(n, r):
    if n == 0 or n == 1:
        return 0
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


a = comb(n, 2)
b = comb(m, 2)
print(a+b)
