n, k = map(int, input().split())
t = []
for i in range(n):
    x = list(map(int, input().split()))
    t.append(x)


ans = []
# x curr
# y  next
def dfs(curr, nex, time=0, visited=[0]):
    time += t[curr][nex]
    visited.append(nex)
    flag = True
    for i in range(n):
        if i not in visited:
            flag = False
            dfs(nex, i, time, visited.copy())

    if flag:
        time += t[nex][0]
        ans.append(time)


for j in range(1, n):
    dfs(0, j, 0, [0].copy())

c = ans.count(k)
print(c)
