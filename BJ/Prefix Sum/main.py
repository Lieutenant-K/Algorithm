import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
d = defaultdict(int)
for i in range(n):
    s, e = map(int, input().split())
    d[s] += 1
    d[e] -= 1

m, cnt = 0, 0
tem, txm = 0, 0
flag = False
for i in sorted(d.keys()):
    cnt += d[i]
    if cnt > m:
        m = cnt
        tem = i
        flag = True
    elif cnt < m and cnt - d[i] == m and flag:
        txm = i
        flag = False
print(m)
print(tem, txm)