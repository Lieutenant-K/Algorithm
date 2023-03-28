import sys
input = sys.stdin.readline
from itertools import combinations

N, L, R, X = map(int, input().split())
A = list(map(int, input().split()))
r = 0
for i in range(2, N+1):
    for comb in combinations(A, i):
        s, l, g = 0, 10**7, 0
        for n in comb:
            s += n
            l = min(l, n)
            g = max(g, n)
        if L <= s <= R and g-l >= X:
            r += 1
print(r)