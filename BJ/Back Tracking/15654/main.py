import sys
input = sys.stdin.readline

def dfs():
    if len(r) == m:
        print(*r)
        return

    for i in s:
        if i not in r:
            r.append(i)
            dfs()
            r.pop()

n, m = map(int, input().split())
s = sorted(list(map(int, input().split())))
r = []
dfs()