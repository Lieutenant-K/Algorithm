import sys
from collections import deque
input = sys.stdin.readline

def roll(i, a, b):
    d = deque([D[j] for j in dir[i//2]])
    d.rotate((-1)**(int(bool(i % 3))))

    if s[a][b] == 0:
        s[a][b] = d[3]
    else:
        d[3] = s[a][b]
        s[a][b] = 0

    for j in range(4):
        D[dir[i//2][j]] = d[j]
    print(d[1])


dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]
dir = [[1, 2, 3, 5], [0, 2, 4, 5]]
D = [0, 0, 0, 0, 0, 0]
n, m, x, y, k = map(int, input().split())
s = [list(map(int, input().split())) for _ in range(n)]
for i in list(map(int, input().split())):
    i -= 1
    nx, ny = x+dx[i], y+dy[i]
    if nx < 0 or nx > n-1 or ny < 0 or ny > m-1:
        continue
    roll(i, nx, ny)
    x, y = nx, ny