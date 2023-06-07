from heapq import heappush, heappop
import sys
input = sys.stdin.readline

def dijkstra(nodes):
    h = []
    distance = [int(1e9)]*len(G)
    for node in nodes:
        distance[node] = 0
        heappush(h, (0, node))

    while h:
        dis, now = heappop(h)

        if distance[now] < dis:
            continue

        for node, cost in G[now]:
            if dis + cost < distance[node]:
                distance[node] = dis + cost
                heappush(h, (dis + cost, node))
    return distance


V, E = map(int, input().split())
G = [set() for _ in range(V+1)]
INF = int(1e9)
for _ in range(E):
    u, v, w = map(int, input().split())
    G[u].add((v, w))
    G[v].add((u, w))
M, x = map(int, input().split())
mac = set(list(map(int, input().split())))
S, y = map(int, input().split())
star = set(list(map(int, input().split())))
house = set(range(1, V+1)) - mac - star
D = list(zip(dijkstra(mac), dijkstra(star)))

r = INF
for i in house:
    a, b = D[i]
    if a <= x and b <= y:
        r = min(r, a + b)

if r == INF:
    print(-1)
else:
    print(r)