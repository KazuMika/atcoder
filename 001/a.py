import sys
from pprint import pprint
sys.setrecursionlimit(10**8)
#h, w = map(int, input().split())
#c = [list(input()) for i in range(h)]
h, w = 4, 4

s = '''
s...
....
....
...g
'''

c = [list(i) for i in s.strip().split('\n')]

for i in range(len(c)):
    for j in range(len(c[0])):
        if c[i][j] == 's':
            sx, sy = i, j
        elif c[i][j] == 'g':
            gx, gy = i, j


def dfs2():
    stack = [[sx, sy]]
    dy = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    while stack:
        pprint(c)
        x, y = stack.pop(0)
        for i in range(len(dy)):
            nx, ny = x + dy[i][0], y+dy[i][1]
            if not(0 <= nx < h) or not(0 <= ny < w) or c[nx][ny] == '#':
                pass
            elif c[nx][ny] == 'g':
                print('Yes')
                exit(0)
            else:
                c[nx][ny] = "#"
                stack.append([nx, ny])


def dfs(x, y):
    if not(0 <= x < h) or not(0 <= y < w) or c[x][y] == "#":
        return

    pprint(c)

    if c[x][y] == "g":
        print("Yes")
        exit(0)

    c[x][y] = '#'
    dfs(x+1, y)
    dfs(x-1, y)
    dfs(x, y+1)
    dfs(x, y-1)

def bfs():



dfs2()
print('No')
