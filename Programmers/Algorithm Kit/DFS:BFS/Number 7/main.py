from collections import deque

def rotate(arr):
    return [list(i)[-1::-1] for i in list(zip(*arr))]


def bfs(arr, a, b, v):
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    q = deque([(a, b)])
    arr[a][b] = 2
    puzzle = []
    puzzle.append((0, 0))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < len(arr) and 0 <= ny < len(arr) and arr[nx][ny] == v:
                arr[nx][ny] = 2
                q.append((nx, ny))
                puzzle.append((nx - a, ny - b))
    return puzzle


def solution(game_board, table):
    answer = 0
    n = len(table)
    puzzles = []
    for x in range(n):
        for y in range(n):
            if table[x][y] == 1:
                puzzles.append(bfs(table, x, y, 1))

    puzzle_shapes = [[] for _ in range(len(puzzles))]
    for i in range(len(puzzles)):
        puzzle_shapes[i].append(puzzles[i])
        mx, my = list(zip(*puzzles[i]))
        m = max(max(mx)-min(mx)+1, max(my)-min(my)+1)
        rect = [[0]*m for _ in range(m)]
        for x, y in puzzles[i]:
            rect[x-min(mx)][y-min(my)] = 1

        rotate_list = [rect, rotate([k[:] for k in rect]), rotate([k[:] for k in rotate([k[:] for k in rect])])]
        for r in rotate_list:
            rotate_rect = rotate([k[:] for k in r])
            for x in range(m):
                for y in range(m):
                    if rotate_rect[x][y] == 1:
                        puzzle_shapes[i].append(bfs(rotate_rect, x, y, 1))

    use = [False] * len(puzzles)
    for x in range(n):
        for y in range(n):
            if game_board[x][y] == 0:
                space = bfs(game_board, x, y, 0)
                for i in range(len(puzzles)):
                    if not use[i] and space in puzzle_shapes[i]:
                        for a, b in space:
                            game_board[x+a][y+b] = 1
                        use[i] = True
                        answer += len(space)
                        break
    # print(game_board)
    return answer