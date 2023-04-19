import sys
input = sys.stdin.readline
sys.setrecursionlimit(1010)

def dfs(x, y, s):
    if x == n:
        print(*s, sep="\n")
        exit()

    visit[x][y] = True
    for k in a[x]:
        if k != y and not visit[x+1][k]:
            dfs(x+1, k, s+str(k))

n = int(input())
a = [list(map(int, input().split()))[1:] for _ in range(n)]
visit = [[False]*10 for _ in range(n+1)]
dfs(0, 0, "")
print(-1)