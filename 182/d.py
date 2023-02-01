n = int(input())
a = list(map(int, input().split()))
com = [a[0]]
nows = [a[0]]

if len(a) == 1:
    print(max(a[0], 0))
    exit(0)

for i in range(1, len(a)):
    com.append(a[i]+com[i-1])
    nows.append(com[i]+nows[i-1])


ans = []
mav = max(nows)
for i in range(nows.index(mav)):
    ans.append(com[i]+mav)

if len(ans) == 0:
    print(a[0])
else:
    print(max(0, max(ans)))
