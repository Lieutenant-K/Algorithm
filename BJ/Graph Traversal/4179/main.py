import sys
input = sys.stdin.readline
from collections import deque

def bfs(m, points, flag):
    q = deque(points)
    while q:
        x, y = q.popleft()
        condition = (x == 0 or x == r - 1 or y == 0 or y == c - 1) if flag else False
        if condition:
            print(m[x][y] + 1)
            exit()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= r or ny < 0 or ny >= c or g[nx][ny] == '#':
                continue

            condition = (m[x][y] + 1 < f[nx][ny]) if flag else True
            if m[nx][ny] == INF and condition:
                q.append((nx, ny))
                m[nx][ny] = m[x][y] + 1

r, c = map(int, input().split())
g = [input().rstrip() for _ in range(r)]
fire = []
INF = 10**7
jx, jy = 0, 0
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
f = [[INF]*c for _ in range(r)]
j = [[INF]*c for _ in range(r)]

for x in range(r):
    for y in range(c):
        if g[x][y] == 'F':
            fire.append((x, y))
            f[x][y] = 0
        if g[x][y] == 'J':
            jx, jy = x, y
            j[x][y] = 0

bfs(f, fire, False)
bfs(j, [(jx, jy)], True)
print("IMPOSSIBLE")