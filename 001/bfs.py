h, w = map(int, input().split())
c = [list(input()) for i in range(h)]
visited = [[0 for i in range(w)] for i in range(h)]
queue = []

for i in range(h):
    for j in range(w):
        if c[i][j] == 's':
            queue.append([i, j])
            visited[i][j] = 1


dy = [[1, 0], [0, 1], [-1, 0], [0, -1]]
while queue:
    x, y = queue.pop(0)
    if c[x][y] == 'g':
        print('Yes')
        exit(0)
    for i in dy:
        nx = x + i[0]
        ny = y + i[1]
        if (0 <= nx < h) and (0 <= ny < w) and c[nx][ny] != '#' and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            queue.append([nx, ny])

print('No')
