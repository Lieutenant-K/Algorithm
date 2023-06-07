import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**4)

V, E = map(int, input().split())
G = [set() for _ in range(V+1)]
for _ in range(E):
    a, b = map(int, input().split())
    G[a].add(b)
    G[b].add(a)
d = len([i for i in range(1, V+1) if len(G[i]) % 2 != 0])

def dfs(x):
    for v in G[x]:
        if not visit[v]:
            visit[v] = True
            dfs(v)

visit = [False]*(V+1)
dfs(1)

if False not in visit[1:] and (d == 0 or d == 2):
    print("YES")
else:
    print("NO")