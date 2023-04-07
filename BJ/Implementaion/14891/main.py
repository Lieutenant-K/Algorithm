import sys
input = sys.stdin.readline

def dfs(idx, dir):
    visit[idx] = True
    if idx-1 >= 0 and not visit[idx-1] and gear[idx][6] != gear[idx-1][2]:
        dfs(idx-1, -dir)
    if idx+1 < 4 and not visit[idx+1] and gear[idx][2] != gear[idx+1][6]:
        dfs(idx+1, -dir)

    gear[idx] = gear[idx][-dir:] + gear[idx][:-dir]
    visit[idx] = False

gear = [list(map(int, input().rstrip())) for _ in range(4)]
k = int(input())
visit = [False]*4
for _ in range(k):
    n, d = map(int, input().split())
    dfs(n-1, d)
print(sum([2**i*gear[i][0] for i in range(4)]))