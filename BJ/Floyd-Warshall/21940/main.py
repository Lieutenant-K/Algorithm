import sys
input = sys.stdin.readline

INF = 1e9
n, m = map(int, input().split())
g = [[INF]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    g[a][b] = c

for k in range(1, n+1):
    g[k][k] = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            if g[i][k] + g[k][j] < g[i][j]:
                g[i][j] = g[i][k] + g[k][j]

k = int(input())
city = list(map(int, input().split()))
MIN = INF
r = []
for i in range(1, n+1):
    v = max([g[c][i] + g[i][c] for c in city])
    r.append((i, v))
    MIN = min(MIN, v)
print(*[i for i, v in sorted(r) if v == MIN])