import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

n = int(input())
a = sorted(list(map(int, input().split())))
cnt = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        v = -a[i]-a[j]
        l = bisect_left(a, v, j+1, n)
        r = bisect_right(a, v, j+1, n)
        cnt += r - l
print(cnt)