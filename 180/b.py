from math import sqrt

n = int(input())
xs = list(map(int, input().split()))
man = sum(abs(x) for x in xs)
yuy = sqrt(sum(x*x for x in xs))
che = max(abs(x) for x in xs)
print(man)
print(yuy)
print(che)
