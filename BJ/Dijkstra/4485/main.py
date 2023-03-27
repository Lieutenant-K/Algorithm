import sys
import heapq
input = sys.stdin.readline

count = 1
while(1):
    N = int(input())

    if N == 0:
        break

    graph = [list(map(int, input().split())) for _ in range(N)]
    distance = [[10*N**2]*N for _ in range(N)]

    queue = []
    heapq.heappush(queue, (graph[0][0], 0, 0))

    while queue:
        d, x, y = heapq.heappop(queue)
        if distance[x][y] < d:
            continue

        dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            cost = d + graph[nx][ny]
            if cost < distance[nx][ny]:
                heapq.heappush(queue, (cost, nx, ny))
                distance[nx][ny] = cost
    print("Problem %d: %d" % (count, distance[N-1][N-1]))
    count += 1