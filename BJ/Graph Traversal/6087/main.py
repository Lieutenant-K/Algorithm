import sys
input = sys.stdin.readline
from collections import deque

def laser(x, y):
    # 하, 상, 우, 좌
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    arr = []
    for k in range(4):
        tx, ty = x, y
        while 0 <= tx + dx[k] < h and 0 <= ty + dy[k] < w and g[tx+dx[k]][ty+dy[k]] != '*':
            tx += dx[k]
            ty += dy[k]
            if g[tx][ty] == '.':
                g[tx][ty] = g[x][y] + 1
                arr.append((tx, ty))
    return arr


w, h = map(int, input().split())
p, g = [], []
for i in range(h):
    row = list(input().rstrip())
    for j in range(w):
        if row[j] == 'C':
            p.append((i, j))
    g.append(row)

sx, sy = p[0]
ex, ey = p[1]
g[sx][sy] = -1
g[ex][ey] = '.'
q = deque([(sx, sy)])

while q:
    x, y = q.popleft()
    q += laser(x, y)

print(g[ex][ey])