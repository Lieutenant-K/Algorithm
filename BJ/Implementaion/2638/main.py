import sys
from collections import deque
input = sys.stdin.readline

dx, dy = [1,-1,0,0], [0,0,1,-1]

def bfs(g):
    queue = deque([(0, 0)])
    melting = [[0]*m for _ in range(n)]
    points = []

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if g[nx][ny] == 0 and melting[nx][ny] >= 0:
                melting[nx][ny] = -1
                queue.append((nx, ny))
            if g[nx][ny] == 1:
                melting[nx][ny] += 1
                if melting[nx][ny] >= 2:
                    g[nx][ny] = -1
                    points.append((nx, ny))

    for x, y in points:
        g[x][y] = 0

    return len(points)

n, m = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]
total = sum([g[i].count(1) for i in range(n)])
r = 0

while total > 0:
    total -= bfs(g)
    r += 1
print(r)