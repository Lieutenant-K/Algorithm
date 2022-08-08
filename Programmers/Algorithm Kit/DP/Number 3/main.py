def solution(m, n, puddles):
    grid = [[0]*(m+1)] + [([0] + [-1]*m) for _ in range(n)]
    grid[1][1] = 1
    for x in puddles:
        grid[x[1]][x[0]] = 0

    for i in range(1, n+1):
        for j in range(1, m+1):
            if grid[i][j] == 0 or (i == 1 and j == 1):
                continue
            grid[i][j] = (grid[i-1][j] + grid[i][j-1])
    return grid[n][m] % (10**9+7)