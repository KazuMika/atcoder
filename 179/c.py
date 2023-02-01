n = int(input())
ans = 0
s = []

for i in range(1, n):
    for j in range(1, n):
        if i * j > n:
            print(i*j)
            exit(0)


print(ans)
