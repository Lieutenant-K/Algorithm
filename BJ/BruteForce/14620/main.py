import sys
input = sys.stdin.readline

def search(x, y):
    dx, dy = [0, 1, -1, 0, 0], [0, 0, 0, 1, -1]
    result = []
    for k in range(5):
        nx, ny = x+dx[k], y+dy[k]
        if not visit[nx][ny]:
            result.append((nx, ny))
    
    return result

def dfs(cnt, answer):
    if cnt == 4:
        global ans
        ans = min(ans, answer)
        return

    for i in range(1, n-1):
        for j in range(1, n-1):
            arr = search(i, j)
            if len(arr) == 5:
                cost_sum = 0
                for x, y in arr:
                    visit[x][y] = True
                    cost_sum += cost[x][y]

                dfs(cnt+1, answer+cost_sum)

                for x, y in arr:
                    visit[x][y] = False


n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]
visit = [[False]*n for _ in range(n)]
ans = 200*100
dfs(1, 0)
print(ans)