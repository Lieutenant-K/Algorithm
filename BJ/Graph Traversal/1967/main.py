import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

def dfs(x):
    m = 0
    for i, j in s[x]:
        d[x].append(j + dfs(i))
        m = max(m, d[x][-1])
    return m

n = int(input())
s = [[] for _ in range(n+1)]
d = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, e = map(int, input().split())
    s[a].append((b, e))
dfs(1)

r = 0
for i in d:
    i.sort(reverse=True)
    r = max(r, sum(i[:2]))
print(r)