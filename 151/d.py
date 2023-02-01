import sys
sys.setrecursionlimit(10 ** 7)
h, w = map(int, input().split())
s = [list(input()) for i in range(h)]

# 3 5
# ...#.
# .#.#.
# .#...
ans = []
def bfs(s, e, counter, sc):
    if not(0 <= s[0] < h) or not(0 <= s[1] < w) or sc[s[0]][s[1]] == '#':
        return
    else:
        if s[0] == e[0] and s[1] == e[1]:
            ans.append(counter)
            return
        sc[sx][sy] = "#"
        bfs(sx+1, sy, counter+1, sc.copy())
        bfs(sx-1, sy, counter+1, sc.copy())
        bfs(sx, sy+1, counter+1, sc.copy())
        bfs(sx, sy-1, counter+1, sc.copy())


for i in range(h):
    for j in range(w):
        for a in range(h):
            for b in range(w):
        if s[i][j] != '#':
            bfs([i, j], [a, b] 0, s.copy())

print(max(ans))
