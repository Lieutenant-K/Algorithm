import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
degree = [set() for _ in range(n+1)]
for _ in range(m):
    seq = list(map(int, input().split()))[1:]
    for i in range(len(seq)-1):
        degree[seq[i+1]].add(seq[i])
queue = [i for i in range(1, n+1) if len(degree[i]) == 0]
result = []
while queue:
    k = queue.pop()
    result.append(str(k))
    for i in range(1, n+1):
        if k in degree[i]:
            degree[i].remove(k)
            if len(degree[i]) == 0:
                queue.append(i)
print("\n".join(result) if len(result) == n else 0)