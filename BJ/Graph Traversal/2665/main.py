import sys
input = sys.stdin.readline
from collections import deque
sys.setrecursionlimit(10**5)

def dfs(i, j, dis):
    p = []
    if i == n-1 and j == n-1:
        global r
        r = dis
        return p

    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    for k in range(4):
        nx, ny = i + dx[k], j + dy[k]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if not visit[nx][ny]:
            visit[nx][ny] = True
            if g[nx][ny] == 1:
                p += dfs(nx, ny, dis)
            else:
                p.append((nx, ny, dis+1))
    return p

n = int(input())
g = [list(map(int, input().rstrip())) for _ in range(n)]
visit = [[False]*n for _ in range(n)]
r = -1
q = deque([(0, 0, 0)])
visit[0][0] = True

while q:
    x, y, d = q.popleft()
    q += dfs(x, y, d)
    if r >= 0:
        print(r)
        exit()