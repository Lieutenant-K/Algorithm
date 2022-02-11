import sys
import pprint
input = sys.stdin.readline

def sol(x, s):

    if x == k:
        if s == n:
            return 1
        return 0

    if d[x][s] > -1:
        return d[x][s]

    d[x][s] = 0
    for i in range(n+1):
        if s+i > n:
            break
        d[x][s] += sol(x+1, s+i) % 10**9

    return d[x][s]

n, k = map(int, input().split())
d = [[-1]*(n+1) for _ in range(k+1)]
print(sol(0, 0) % 10**9)