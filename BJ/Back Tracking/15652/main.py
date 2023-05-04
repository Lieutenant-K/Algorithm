def dfs(idx):
    if len(r) == m:
        print(*r)
        return

    for i in range(idx, n+1):
        r.append(i)
        dfs(i)
        r.pop()

n, m = map(int, input().split())
r = []
dfs(1)