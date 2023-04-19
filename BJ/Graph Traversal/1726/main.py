import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
g = [[0]*(m+1)] + [[0] + list(map(int, input().split())) for _ in range(n)]
v = [[[0]*5 for _ in range(m+1)] for _ in range(n+1)]
start = tuple(map(int, input().split()))
end = tuple(map(int, input().split()))
q = deque([start])

while q:
    dx, dy = [0, 0, 0, 1, -1], [0, 1, -1, 0, 0]
    x, y, d = q.popleft()

    if (x, y, d) == end:
        print(v[x][y][d])
        break

    direct = [3, 4] if d < 3 else [1, 2]
    for k in direct:
        if v[x][y][k] == 0:
            v[x][y][k] = v[x][y][d] + 1
            q.append((x, y, k))

    for i in range(1, 4):
        nx, ny = x + i*dx[d], y + i*dy[d]
        if nx < 1 or nx > n or ny < 1 or ny > m or g[nx][ny] == 1:
            break
        if v[nx][ny][d] == 0:
            v[nx][ny][d] = v[x][y][d] + 1
            q.append((nx, ny, d))