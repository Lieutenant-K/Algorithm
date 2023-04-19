import sys
input = sys.stdin.readline
sys.setrecursionlimit(2001)

def dfs(s, e, i):
    if s == e:
        d[s][e] = v[s]*i
        return d[s][e]

    if d[s][e] > 0:
        return d[s][e]

    v1 = v[s]*i + dfs(s+1, e, i+1)
    v2 = v[e]*i + dfs(s, e-1, i+1)
    d[s][e] = max(v1, v2)

    return d[s][e]

n = int(input())
v = [int(input()) for _ in range(n)]
s, e = 0, n-1
r, t = 0, 1
d = [[0]*n for _ in range(n)]
dfs(0, n-1, 1)
print(d[0][n-1])