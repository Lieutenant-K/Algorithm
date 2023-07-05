import sys
input = sys.stdin.readline
from collections import deque

def bfs(x, y):
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    q = deque([(x, y)])
    g[x][y] = 0
    cnt = 1

    while q:
        a, b = q.popleft()
        for k in range(4):
            nx, ny = a + dx[k], b + dy[k]
            if 0 <= nx < n and 0 <= ny < m and g[nx][ny]:
                g[nx][ny] = 0
                q.append((nx, ny))
                cnt += 1
    return cnt

n, m = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]
r1, r2 = 0, 0
for i in range(n):
    for j in range(m):
        if g[i][j]:
            r1 += 1
            r2 = max(r2, bfs(i, j))
print(r1, r2, sep="\n")