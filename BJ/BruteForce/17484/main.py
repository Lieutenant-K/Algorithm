import sys
input = sys.stdin.readline

def dfs(x, y, r, pre):
    if x == n-1:
        global result
        result = min(result, r)
        return

    d = [-1, 0, 1]
    for k in range(3):
        if 0 <= y+d[k] < m and k != pre:
            dfs(x+1, y+d[k], r+g[x+1][y+d[k]], k)


n, m = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]
result = 1e9
for i in range(m):
    dfs(0, i, g[0][i], -1)
print(result)