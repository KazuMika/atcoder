n = int(input())
ps = list(map(int, input().split()))
ans = 0

for i in range(1, len(ps)-1):
    s1 = ps[i-1] < ps[i] and ps[i+1] > ps[i]
    s2 = ps[i-1] > ps[i] and ps[i+1] < ps[i]
    if s1 or s2:
        ans += 1


print(ans)
