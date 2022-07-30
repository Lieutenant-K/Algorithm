from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    maps = [[0] * 101 for _ in range(101)]
    for x1, y1, x2, y2 in rectangle:
        for c in range(x1 * 2, x2 * 2 + 1):
            for r in range(y1 * 2, y2 * 2 + 1):
                maps[r][c] = 1

    for x1, y1, x2, y2 in rectangle:
        for c in range(2 * x1 + 1, x2 * 2):
            for r in range(2 * y1 + 1, 2 * y2):
                maps[r][c] = 0

    q = deque([(2 * characterX, 2 * characterY)])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < 101 and 0 <= ny < 101 and maps[ny][nx] == 1:
                maps[ny][nx] = maps[y][x] + 1
                q.append((nx, ny))

    return maps[2 * itemY][2 * itemX] // 2