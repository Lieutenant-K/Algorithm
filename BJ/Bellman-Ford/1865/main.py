import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, m, w = map(int, input().split())
    g = [[] for _ in range(n+1)]
    for i in range(m + w):
        a, b, c = map(int, input().split())
        if i < m:
            g[a].append((b, c))
            g[b].append((a, c))
        else:
            g[a].append((b, -c))

    d = [0]*(n+1)
    flag = False
    for k in range(n):
        for i in range(1, n+1):
            for node, cost in g[i]:
                if d[i] + cost < d[node]:
                    d[node] = d[i] + cost
                    if k == n-1:
                        flag = True
    print("YES" if flag else "NO")