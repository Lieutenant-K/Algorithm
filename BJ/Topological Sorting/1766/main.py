import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
d = [[[], 0] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    d[a][0].append(b)
    d[b][1] += 1

q = [i for i in range(1, n+1) if d[i][1] == 0]

while q:
    k = heapq.heappop(q)
    print(k, end=' ')
    for i in d[k][0]:
        d[i][1] -= 1
        if not d[i][1]:
            heapq.heappush(q, i)