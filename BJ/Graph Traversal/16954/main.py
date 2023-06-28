import sys
input = sys.stdin.readline

G = [input().rstrip() for _ in range(8)]
W = set([(i, j) for i in range(8) for j in range(8) if G[i][j] == '#'])
dx, dy = [0, -1, -1, 0, 1, 1, 1, 0, -1], [0, 0, 1, 1, 1, 0, -1, -1, -1]

P = [set() for _ in range(9)]
P[0].add((7, 0))
for i in range(8):
    for x, y in P[i]:
        for k in range(9):
            nx, ny = x + dx[k], y + dy[k]
            if nx < 0 or nx > 7 or ny < 0 or ny > 7:
                continue
            if (nx - i, ny) not in W and (nx - i - 1, ny) not in W:
                P[i+1].add((nx, ny))
print(int(bool(P[8])))