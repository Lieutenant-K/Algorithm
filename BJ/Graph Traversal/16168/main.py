import sys
from sys import stdin
sys.setrecursionlimit(10**5)

def dfs(x):
    for v in g[x]:
        if v not in visit:
            visit.add(v)
            dfs(v)

v, e = map(int, stdin.readline().split(" "))
g = [set() for _ in range(v)]
for _ in range(e):
    a, b = map(int, stdin.readline().split(" "))
    g[a-1].add(b-1)
    g[b-1].add(a-1)
visit = set()
dfs(0)
if visit == set(range(v)):
    degree = list(map(lambda x: True if len(x) % 2 == 0 else False, g))
    if degree.count(False) == 2 or False not in degree:
        print("YES")
    else:
        print("NO")
else:
    print("NO")