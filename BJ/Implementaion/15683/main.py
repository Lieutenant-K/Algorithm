import sys
input = sys.stdin.readline

def move(i, j, direction, v):
    r = 0
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
    for d in direction:
        di, dj = 0, 0
        while 0 <= i+di < n and 0 <= j+dj < m and g[i+di][j+dj] != 6:
            if g[i+di][j+dj] <= 0:
                if g[i+di][j+dj] == 0:
                    r += 1
                g[i + di][j + dj] += v

            di += dx[d]
            dj += dy[d]
    return r

def dfs(idx, cnt):
    if idx == len(cctv):
        global result
        result = max(result, cnt)
        return

    x, y, number = cctv[idx]
    for i in range(4):
        d = [[i], [i, i+2], [i, (i+1) % 4], [i, (i+1) % 4, (i+2) % 4], [0, 1, 2, 3]]

        if (i >= 2 and number == 2) or (i >= 1 and number == 5):
            break

        dfs(idx + 1, cnt + move(x, y, d[number-1], -1))
        move(x, y, d[number-1], 1)


n, m = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]
cctv = [(x, y, g[x][y]) for x in range(n) for y in range(m) if 6 > g[x][y] > 0]
wall = [(x, y, g[x][y]) for x in range(n) for y in range(m) if g[x][y] == 6]
result = 0
dfs(0, 0)
print(n*m - len(cctv) - len(wall) - result)