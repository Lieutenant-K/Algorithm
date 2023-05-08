import sys
input = sys.stdin.readline

while(True):
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    g = [list(map(int, input().split())) for _ in range(n)]
    d = [[0]*(m+1) for _ in range(n+1)]
    r = 0
    for x in range(1, n+1):
        for y in range(1, m+1):
            if g[x-1][y-1] == 1:
                d[x][y] = min(d[x-1][y], d[x][y-1], d[x-1][y-1]) + 1
                r = max(r, d[x][y])
    print(r)
