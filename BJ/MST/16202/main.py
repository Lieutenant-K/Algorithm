import sys
input = sys.stdin.readline

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    px, py = parent[x], parent[y]
    parent[px] = py

n, m, k = map(int, input().split())
edges = [tuple(list(map(int, input().split())) + [i+1]) for i in range(m)]
edges.sort(key=lambda x: x[2])
for _ in range(k):
    parent = list(range(n+1))
    mst, cost = [], 0
    for a, b, w in edges:
        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            mst.append((a, b, w))
            cost += w
        if len(mst) == n-1:
            break

    if len(mst) == n-1:
        print(cost, end=" ")
        edges = edges[1:]
    else:
        print(0, end=" ")