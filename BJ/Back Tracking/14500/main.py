import sys
from itertools import combinations
input = sys.stdin.readline

def dfs(x, y, r, cnt):
    global result

    if cnt == 4:
        result = max(result, r)
        return

    next = []
    visit[x][y] = True
    for k in range(4):
        nx, ny = x+dx[k], y+dy[k]
        if 0 <= nx < n and 0 <= ny < m and not visit[nx][ny]:
            next.append(g[nx][ny])
            dfs(nx, ny, r + g[nx][ny], cnt+1)
    visit[x][y] = False

    if cnt == 2 and len(next) >= 2:
        for a, b in combinations(next, 2):
            result = max(result, r + a + b)

n, m = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]
visit = [[False]*m for _ in range(n)]
result = 0
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

for i in range(n):
    for j in range(m):
        dfs(i, j, g[i][j], 1)
print(result)