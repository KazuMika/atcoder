n = int(input())
P = list(map(int, input().split()))
c = 1
minv = P[0]  # その数より左にあるかずは全大きくさくなければならない
for i in range(1, len(P)):
    if minv > P[i]:
        c += 1
    minv = min(minv, P[i])
print(c)
