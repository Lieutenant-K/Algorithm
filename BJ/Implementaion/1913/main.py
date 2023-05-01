import sys
input = sys.stdin.readline

n = int(input())
target = int(input())
g = [[0]*n for _ in range(n)]
x, y = n // 2, n // 2
tx, ty = x, y
g[x][y] = 1
d, t, cnt = 0, 0, 1
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
while x != 0 or y != 0:

    for _ in range(t // 2 + 1):
        x, y = x+dx[d], y+dy[d]
        cnt += 1
        g[x][y] = cnt
        if target == cnt:
            tx, ty = x, y
        if x == 0 and y == 0:
            break

    d = (d+1) % 4
    t += 1

for r in g:
    print(*r, sep=" ")
print(tx+1, ty+1)