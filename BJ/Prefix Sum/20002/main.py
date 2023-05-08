import sys
input = sys.stdin.readline

n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]
d = [[0]*(n+1) for _ in range(n+1)]
r = -1000 * n * n

for i in range(1, n+1):
    for j in range(1, n+1):
        d[i][j] = d[i-1][j] + d[i][j-1] - d[i-1][j-1] + g[i-1][j-1]

for k in range(n):
    for i in range(1, n-k+1):
        for j in range(1, n-k+1):
            v = d[i+k][j+k] - d[i-1][j+k] - d[i+k][j-1] + d[i-1][j-1]
            if r < v:
                r = v
print(r)