import sys
input = sys.stdin.readline

def dfs(x, cnt):
    if cnt == k:
        print(*t, sep="\n")
        # exit()

    for e in g[x]:
        d[e] += 1

    for i in range(x+1, n+1):
        if d[i] == cnt:
            t.append(i)
            dfs(i, cnt+1)
            t.pop()

    for e in g[x]:
        d[e] -= 1

k, n, f = map(int, input().rstrip().split())
g = [[] for _ in range(n+1)]
d = [0]*(n+1)
result = []

for _ in range(f):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

for i in range(1, n+1):
    t = [i]
    dfs(i, 1)

print(-1)