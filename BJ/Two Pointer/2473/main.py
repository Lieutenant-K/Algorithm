import sys
input = sys.stdin.readline

n = int(input())
d = sorted(list(map(int, input().split())))
m = 3*(10**9)
r = []

for i in range(n-2):
    s, e = i+1, n-1
    while s < e:
        v = d[i] + d[s] + d[e]
        if m > abs(v):
            m = abs(v)
            r = [d[i], d[s], d[e]]

        if v > 0:
            e -= 1
        elif v == 0:
            print(d[i], d[s], d[e])
            exit()
        else:
            s += 1
print(*r, sep=' ')