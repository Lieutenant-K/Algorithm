import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    px, py = find(x), find(y)
    if px != py:
        if px > py:
            parent[px] = py
        else:
            parent[py] = px

n, m = map(int, input().split())
parent = list(range(0, n+1))
for _ in range(m):
    op, a, b = map(int, input().split())
    if op == 0:
        union(a, b)
    else:
        print("YES" if find(a) == find(b) else "NO")