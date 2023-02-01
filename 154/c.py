n = int(input())
A = list(map(int, input().split()))
d = {}

for i in A:
    if i in d:
        print("NO")
        exit(0)
    else:
        d[i] = 1

print("YES")
