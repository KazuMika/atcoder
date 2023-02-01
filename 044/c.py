import itertools
n, a = map(int, input().split())
x = list(map(int, input().split()))
xx = []
counter = 0

for i in range(1, n+1):
    for j in itertools.combinations(x, i):
        print(counter)
        temp = list(j)
        if sum(temp) / len(temp) == float(a):
            counter += 1

print(counter)
