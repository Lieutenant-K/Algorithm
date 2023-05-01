import sys
input = sys.stdin.readline

INF = 1e9
n, m = map(int, input().split())
g = [[INF]*(n+1) for _ in range(n+1)]
r = [list(range(n+1)) for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    g[a][b] = c
    g[b][a] = c

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j:
                g[i][j] = 0
                r[i][j] = "-"
                continue

            v = g[i][k] + g[k][j]
            if v < g[i][j]:
                g[i][j] = v
                r[i][j] = r[i][k]

for row in r[1:]:
    print(*row[1:])