import sys
input = sys.stdin.readline

n = int(input())
g = [[0]*101 for _ in range(101)]
dx, dy = [0, -1, 0, 1], [1, 0, -1, 0]
for _ in range(n):
    a, b, d, cnt = map(int, input().split())
    g[b][a] = 1
    x, y = b, a

    x, y = x+dx[d], y+dy[d]
    g[x][y] = 1
    move = [d]

    for i in range(cnt):
        new = []
        for m in move:
            di = (m+1) % 4
            x, y = x+dx[di], y+dy[di]
            g[x][y] = 1
            new.append(di)
        move = new[::-1] + move

result = 0
for i in range(100):
    for j in range(100):
        if g[i][j] == 1 and g[i+1][j] == 1 and g[i][j+1] == 1 and g[i+1][j+1] == 1:
            result += 1
print(result)