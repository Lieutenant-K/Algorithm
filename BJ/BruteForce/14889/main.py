import sys
input = sys.stdin.readline
from itertools import combinations

n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]
d = dict()
for comb in combinations(range(n), n//2):
    r = 0
    for i in range(len(comb)-1):
        for j in range(i+1, len(comb)):
            a, b = comb[i], comb[j]
            r += g[a][b] + g[b][a]
    d[comb] = r

result = (n**2)*(10**2)
for key in d.keys():
    k = tuple(set(range(n)) - set(key))
    result = min(result, abs(d[key] - d[k]))
print(result)