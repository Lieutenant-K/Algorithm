import sys
input = sys.stdin.readline

n, m = map(int, input().split())
x, y, d = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
result = 0
while(1):
    if g[x][y] == 0:
        g[x][y] = 2
        result += 1

    exist = False
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < n and 0 <= ny < m and g[nx][ny] == 0:
            exist = True
            break

    if exist:
        d = (d+3) % 4
        nx, ny = x+dx[d], y+dy[d]
        if 0 <= nx < n and 0 <= ny < m and g[nx][ny] == 0:
            x = nx
            y = ny
    else:
        nx, ny = x+dx[(d+2) % 4], y+dy[(d+2) % 4]
        if nx < 0 or nx >= n or ny < 0 or ny >= m or g[nx][ny] == 1:
            break
        x = nx
        y = ny
print(result)