import sys
from collections import deque

input = sys.stdin.readline

dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0]


def bfs(a, b):
    dis = [[-1] * N for _ in range(N)]
    dis[a][b] = 0
    q = deque([(a, b)])
    global w, r, cnt, X, Y

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx > N - 1 or ny < 0 or ny > N - 1:
                continue
            if S[nx][ny] <= w and dis[nx][ny] < 0:
                dis[nx][ny] = dis[x][y] + 1
                q.append((nx, ny))

    m = N ** 2
    x, y = -1, -1
    for i in range(N):
        for j in range(N):
            if 0 < dis[i][j] < m and 0 < S[i][j] < w:
                x, y = i, j
                m = dis[i][j]

    if m < N ** 2:
        S[a][b], S[x][y] = 0, 0
        X, Y = x, y
        cnt += 1
        if cnt == w:
            cnt = 0
            w += 1
        r += m
        return m

    return 0


N = int(input())
S = [[] for _ in range(N)]
X, Y, cnt, r, w = 0, 0, 0, 0, 2

for i in range(N):
    s = list(map(int, input().split()))
    for j in range(N):
        S[i].append(s[j])
        if s[j] == 9:
            X, Y = i, j

while bfs(X, Y) > 0:
    continue
print(r)