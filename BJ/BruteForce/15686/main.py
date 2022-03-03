import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
s, h, c = [], [], []
for i in range(n):
    s.append(list(map(int, input().split())))
    for j in range(n):
        if s[i][j] == 1:
            h.append((i, j))
        elif s[i][j] == 2:
            c.append((i, j))


print(min([sum([min([abs(nx-x)+abs(ny-y) for nx, ny in list(k)]) for x, y in h]) for k in combinations(c, m)]))