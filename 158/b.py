n, a, b = map(int, input().split())

x = (n // (a+b))
y = (n % (a+b))
y = min(y, a)

if x >= 1:
    print(x*a+y)
else:
    print(min(n, a))
