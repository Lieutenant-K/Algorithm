import sys
input = sys.stdin.readline

n = int(input())
d = list(map(int, input().split()))
s, e = 0, n-1
r = 0
while s < e:
    r = max(r, min(d[s], d[e])*(e-s-1))
    if d[s] <= d[e]:
        s += 1
    else:
        e -= 1
print(r)