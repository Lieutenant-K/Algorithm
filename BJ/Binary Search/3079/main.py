import sys
input = sys.stdin.readline

n, k = map(int, input().split())
t = sorted([int(input()) for _ in range(n)])
s, e, r = 1, t[0] * k, 0

while s <= e:
    m = (s+e)//2
    cnt = sum([m//i for i in t])

    if cnt >= k:
        e = m-1
        r = m
    else:
        s = m+1
print(r)