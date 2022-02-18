import sys
input = sys.stdin.readline

n, k = map(int, input().split())
t, p = [], []
for _ in range(n):
    tit, po = input().split()
    t.append(tit)
    p.append(int(po))

for _ in range(k):
    s, e = 0, n-1
    v = int(input())
    while s <= e:
        m = (s + e) // 2
        if v <= p[m]:
            e = m-1
        else:
            s = m+1
    print(t[s])