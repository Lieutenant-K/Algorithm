import sys
input = sys.stdin.readline

n, m = map(int, input().split())
g = [[] for _ in range(n+1)]
d = [0]*(n+1)
for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    d[b] += 1

q = [i for i in range(1, n+1) if d[i] == 0]
r = []
while q:
    k = q.pop()
    r.append(k)
    for e in g[k]:
        d[e] -= 1
        if d[e] == 0:
            q.append(e)
print(*r, sep=" ")