n, m = map(int, input().split())
a = list(map(int, input().split()))
border = sum(a) / (4 * m)
a.sort(reverse=True)

for i in range(m):
    if border <= a[i]:
        pass
    else:
        print('No')
        exit(0)

print('Yes')
