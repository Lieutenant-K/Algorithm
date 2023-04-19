import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
s = list(reversed(list(map(int, input().split()))))
r = list(range(1, n+1))
q = deque()
for i in range(n):
    if s[i] == 1:
        q.appendleft(r[i])
    elif s[i] == 2:
        k = q.popleft()
        q.appendleft(r[i])
        q.appendleft(k)
    else:
        q.append(r[i])
print(*q)