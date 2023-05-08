import sys
input = sys.stdin.readline
import math

N, A, B, C, D = map(int, input().split())
hn, hk, rn, rk = (C, D, A, B) if B * C > D * A else (A, B, C, D)
r = []
for i in range(hn):
    if N-i*rn < 0:
        r.append(i*rk)
        break
    r.append(i*rk + math.ceil((N-i*rn)/hn)*hk)
print(min(r))