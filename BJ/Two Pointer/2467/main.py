import sys
input = sys.stdin.readline

n = int(input())
d = list(map(int, input().split()))
s, e = 0, n-1
m = 2*(10**9)
r = []
while s < e:
    v = d[s] + d[e]
    if m > abs(v):
        m = abs(v)
        r = [d[s], d[e]]
    if v < 0:
        s += 1
    elif v == 0:
        print(d[s], d[e])
        exit(0)
    else:
        e -= 1
print(*r, sep=' ')