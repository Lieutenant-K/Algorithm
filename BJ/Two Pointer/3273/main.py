import sys
input = sys.stdin.readline

n = int(input())
a = sorted(list(map(int, input().split())))
x = int(input())

s, e = 0, n-1
r = set()
while s < e:
    v = a[s] + a[e]
    if v > x:
        e -= 1
    else:
        if v == x:
            r.add((a[s], a[e]))
        s += 1
print(len(r))