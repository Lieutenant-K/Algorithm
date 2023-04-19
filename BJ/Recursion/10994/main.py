import sys
input = sys.stdin.readline

def star(x, y, k):
    if k == 0:
        return

    l = 4*k-3
    for i in range(y, y+l):
        g[x][i] = "*"
        g[x+l-1][i] = "*"

    for i in range(x, x+l-1):
        g[i][y] = "*"
        g[i][y+l-1] = "*"

    star(x+2, y+2, k-1)


n = int(input())
g = [[" "]*(4*n-3) for _ in range(4*n-3)]
star(0, 0, n)
for r in g:
    print(*r, sep="")