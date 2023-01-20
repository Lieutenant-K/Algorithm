from collections import deque
import pprint
def solution(rectangle, characterX, characterY, itemX, itemY):
    rect = list(zip(*rectangle))
    max_x, max_y = 2*max(rect[2])+1, 2*max(rect[3])+1
    print(max_x, max_y)
    maps = [[0]*(max_x + 1) for _ in range(max_y + 1)]
    dx, dy = [1, -1, 0, 0, 1, 1, -1, -1], [0, 0, 1, -1, 1, -1, 1, -1]
    points = []
    for a, b, c, d in rectangle:
        for i in range(2*b, 2*d+1):
            for j in range(2*a, 2*c+1):
                maps[i][j] = 1
    for a, b, c, d in rectangle:
        for i in range(2*b+1, 2*d):
            for j in range(2*a+1, 2*c):
                maps[i][j] = 0

    queue = deque([(2*characterY, 2*characterX)])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))
    return (maps[2*itemY][2*itemX]-1)//2

sol = solution([[1,1,5,7]], 1, 1, 4, 7)
print(sol)