import sys
from itertools import permutations
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))
cnt = 0
for per in permutations(range(n), n):
    weight = 500
    flag = True
    for p in per:
        weight = weight - k + a[p]
        if weight < 500:
            flag = False
            break
    if flag:
        cnt += 1
print(cnt)