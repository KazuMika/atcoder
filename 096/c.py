from itertools import product

h, w = map(int, input().split())
s = [list(input()) for i in range(h)]
visited = []

def dfs(p):
    if s[p[0]][p[1]] == '.':  # p[0]gatate , p[1] gayoko
        return None

    temp = [1 if s[p[0]+y][p[1]+x] == '#' else 0 for (x, y) in [[1, 0], [0, 1], [0, -1], [-1, 0]] if 0 <= y+p[0] < h and 0 <= x+p[1] < w]
    if sum(temp) <= 0:
        print('No')
        exit(0)


for i in range(len(s)):
    for j in range(len(s[0])):
        dfs([i, j])
print('Yes')
