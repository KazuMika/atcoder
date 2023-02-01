k, n = map(int, input().split())

a = list(map(int, input().split()))

ans = []

diss = []
suma = 0

for i in range(len(a)-1):
    dis = a[i+1] - a[i]
    diss.append(dis)


diss.append(k-a[-1]+a[0])
diss.pop(diss.index(max(diss)))
print(sum(diss))
