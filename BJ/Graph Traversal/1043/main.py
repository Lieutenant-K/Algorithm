import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
q = deque(list(map(int, input().split()))[1:])
party = [list(map(int, input().split()))[1:] for _ in range(m)]
g = [set() for _ in range(n+1)]
visit = [False]*(n+1)
for i in range(1, n+1):
    for j in range(m):
        if i in party[j]:
            g[i] |= (set(party[j]) - {i})

for k in q:
    visit[k] = True

while q:
    k = q.popleft()
    for i in g[k]:
        if not visit[i]:
            q.append(i)
            visit[i] = True

result = 0
for p in party:
    if True in [visit[i] for i in p]:
        continue
    result += 1

print(result)