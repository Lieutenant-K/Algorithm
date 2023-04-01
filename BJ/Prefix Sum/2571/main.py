import sys
input = sys.stdin.readline

n = int(input())
r = 101
g = [[0]*r for _ in range(r)]
m = 100

for _ in range(n):
    a, b = map(int, input().split())
    for i in range(10):
        for j in range(10):
            g[a+i][b+j] = 1

for i in range(r):
    for j in range(1, r):
        if g[j][i] == 1:
            g[j][i] += g[j-1][i]

for i in range(r):
    for j in range(r):
        if g[i][j] > 0:
            y = j
            h = g[i][j]
            while y < r and g[i][y] > 0:
                h = min(h, g[i][y])
                m = max(m, (h)*(y-j+1))
                y += 1
print(m)