import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N, M = map(int, input().split())
G = [[] for _ in range(N+1)]
for _ in range(M):
    A, B, C = map(int, input().split())
    G[A].append((B, C))
    G[B].append((A, C))
S, E = map(int, input().split())
D = [0]*(N+1)

D[S] = 10**9
h = []
heappush(h, (-10**9, S))
while h:
    weight, node = heappop(h)
    weight = -weight

    if D[node] > weight:
        continue

    for v, w in G[node]:
        d = w if weight >= w else weight
        if D[v] < d:
            D[v] = d
            heappush(h, (-d, v))
print(D[E])