from collections import deque

def find_puzzle(graph, value, i, j):
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    n = len(graph)
    puzzle, queue = [(0, 0)], deque([(i, j)])
    graph[i][j] = int(not value)
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == value:
                graph[nx][ny] = int(not value)
                queue.append((nx, ny))
                puzzle.append((nx - i, ny - j))
    return puzzle


def bfs(graph, value):
    n = len(graph)
    return [find_puzzle(graph, value, i, j) for i in range(n) for j in range(n) if graph[i][j] == value]

def solution(game_board, table):
    puzzles = bfs(table, True)
    empties = bfs(game_board, False)
    variations, used, answer = [], [], 0

    for puzzle in puzzles:
        min_y = min(map(lambda x: x[1], puzzle))
        puzzle = list(map(lambda x: (x[0], x[1] + abs(min_y)), puzzle))
        m = max(map(max, *zip(*puzzle)))
        space = [[0] * (m + 1) for _ in range(m + 1)]

        for a, b in puzzle:
            space[a][b] = 1

        var = []
        for i in range(4):
            variation = bfs([row[:] for row in space], True)
            var.append(variation[0])
            space = [list(array[::-1]) for array in list(zip(*space))]
        variations.append(var)

    for empty in empties:
        for i, var in enumerate(variations):
            if i in used:
                continue
            if set(empty) in list(map(set, var)):
                used.append(i)
                answer += len(empty)
                break

    return answer
