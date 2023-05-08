import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
op = [tuple(map(int, input().split())) for _ in range(M)]
dx, dy = [0, 0, -1, -1, -1, 0, 1, 1, 1], [0, -1, -1, 0, 1, 1, 1, 0, -1]
cloud = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]

for d, s in op:
    nc = []
    for cx, cy in cloud:
        ncx, ncy = cx + s * dx[d], cy + s * dy[d]
        if ncx < 0 or ncx >= N:
            ncx = (ncx + N) % N
        if ncy < 0 or ncy >= N:
            ncy = (ncy + N) % N
        nc.append((ncx, ncy))

    for x, y in nc:
        A[x][y] += 1

    for x, y in nc:
        cnt = 0
        for i in range(1, 5):
            nx, ny = x + dx[2 * i], y + dy[2 * i]
            if 0 <= nx < N and 0 <= ny < N and A[nx][ny] > 0:
                cnt += 1
        A[x][y] += cnt
    
    nc = set(nc)
    cloud = []
    for x in range(N):
        for y in range(N):
            if A[x][y] > 1 and (x, y) not in nc:
                cloud.append((x, y))
                A[x][y] -= 2

r = sum([A[x][y] for x in range(N) for y in range(N)])
print(r)