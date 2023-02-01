n, k = map(int, input().split())
P = list(map(int, input().split()))
maxv = 0
maxi = None
for i in range(0, len(P)-k):
    b = sum(P[i:i+k])
    if maxv < b:
        maxv = b
        maxi = i


ans = 0
for i in P[maxi:maxi+k]:
    ans += sum(list(range(1, i+1))) / i
print(ans)
