import sys
input = sys.stdin.readline

def dfs(idx, r):
    if len(r) == m:
        print(*r)
        return

    for i in range(idx, n):
        dfs(i, r+[s[i]])

n, m = map(int, input().split())
s = sorted(list(map(int, input().split())))
dfs(0, [])