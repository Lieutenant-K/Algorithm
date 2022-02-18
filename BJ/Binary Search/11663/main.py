import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

n, k = map(int, input().split())
p = sorted(list(map(int, input().split())))
for _ in range(k):
    l, r = map(int, input().split())
    print(bisect_right(p,r) - bisect_left(p,l))