import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x, y):
    global r
    if d[x][y] > 0:
        return d[x][y]

    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    m = 0
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < n and 0 <= ny < n and g[x][y] < g[nx][ny]:
            m = max(m, dfs(nx, ny))

    d[x][y] = m+1
    r = max(r, m+1)
    return m+1

n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]
d = [[0]*n for _ in range(n)]
r = 0
for i in range(n):
    for j in range(n):
        dfs(i, j)

print(r)