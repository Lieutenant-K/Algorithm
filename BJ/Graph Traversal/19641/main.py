import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x, parent):
    global cnt
    cnt += 1
    d[x][0] = cnt

    for node in g[x]:
        if node != parent:
            dfs(node, x)

    cnt += 1
    d[x][1] = cnt

n = int(input())
g = [[] for _ in range(n+1)]
d = [[0]*2 for _ in range(n+1)]
for _ in range(n):
    a = list(map(int, input().split()))
    g[a[0]] = sorted(a[1:-1])
s = int(input())

cnt = 0
dfs(s, 0)

for i in range(1, n+1):
    print(i, d[i][0], d[i][1])