x, n = map(int, input().split())
ps = list(map(int, input().split()))
pss = [i for i in range(-1000, 1000)]
ps = list(filter(lambda i: i not in ps, pss))
ans = x

for i, p in enumerate(ps):
    temp = abs(x-p)
    if i == 0:
        mins = temp
        ans = p
    else:
        if mins > temp:
            mins = temp
            ans = p
        elif mins == temp:
            if ans > p:
                ans = p

print(ans)
