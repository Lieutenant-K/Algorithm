import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
s = [[] for _ in range(n+1)]
d, r = [0]*(n+1), [0]*(n+1)
q = deque([])
for _ in range(m):
    a, b = map(int, input().split())
    s[a].append(b)
    d[b] += 1

for i in range(1, n+1):
    if d[i] == 0:
        q.append(i)
        r[i] = 1

while q:
    k = q.popleft()
    for i in s[k]:
        d[i] -= 1
        if d[i] == 0:
            q.append(i)
            r[i] = r[k]+1
print(*r[1:], sep=' ')