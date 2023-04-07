import sys
input = sys.stdin.readline

def move():
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    visit = [[0] * c for _ in range(r)]
    for x in range(r):
        for y in range(c):
            if g[x][y] > 0:
                cnt = 0
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if 0 <= nx < r and 0 <= ny < c and g[nx][ny] != -1:
                        visit[nx][ny] += g[x][y] // 5
                        cnt += 1
                visit[x][y] += -cnt * (g[x][y] // 5)

    for x in range(r):
        for y in range(c):
            g[x][y] += visit[x][y]

def rotate(s, e, d):
    idx1 = [(s, i) for i in range(c)][:-1] + [(i, c-1) for i in range(s, e+1)][:-1]
    idx2 = [(e, i) for i in range(c-1, -1, -1)][:-1] + [(i, 0) for i in range(e, s-1, -1)][:-1]
    idx = idx1 + idx2

    array = [g[i][j] for i, j in idx]
    array = array[d:] + array[:d]

    for i in range(len(idx)):
        x, y = idx[i]
        g[x][y] = array[i] if array[i] != -1 else 0

    h = e if d == 1 else s
    g[h][0] = -1


r, c, t = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(r)]
a = [i for i in range(r) if g[i][0] == -1][0]
for _ in range(t):
    move()
    rotate(0, a, 1)
    rotate(a + 1, r - 1, -1)

result = sum([g[i][j] for i in range(r) for j in range(c) if g[i][j] > 0])
print(result)