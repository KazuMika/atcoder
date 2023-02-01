n = int(input())
points = [list(map(int, input().split())) for i in range(n)]

for i in range(n):
    x0, y0 = points[i]
    for j in range(i+1, n):
        x1, y1 = points[j]
        for k in range(j+1, n):
            x2, y2 = points[k]
            if (x0-x1)*(y1-y2) == (x1-x2) * (y0-y1):
                print("Yes")
                exit(0)

print('No')
