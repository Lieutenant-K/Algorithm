from collections import deque
def solution(maps):
    n, m = len(maps), len(maps[0])
    dx, dy = [1,-1,0,0], [0,0,1,-1]
    queue = deque([(0, 0)])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))
    return maps[n-1][m-1] if maps[n-1][m-1] != 1 else -1
