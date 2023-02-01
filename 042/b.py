N, L = map(int, input().split())
strs = []

for i in range(N):
    strs.append(input())

for i in range(len(strs)-1, 1, -1):
    for j in range(i):
        if strs[j] > strs[j+1]:
            strs[j], strs[j+1] = strs[j+1], strs[j]

print(''.join(strs))
