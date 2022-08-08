from collections import deque
def solution(maps):
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    answer = 0
    n, m = len(maps[-1]), len(maps)
    q = deque([(0, 0)])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y+ dy[i]
            if 0 <= nx < m and 0 <= ny < n and maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                q.append((nx, ny))
    answer = maps[m-1][n-1] if maps[m-1][n-1] > 1 else -1
    return answer