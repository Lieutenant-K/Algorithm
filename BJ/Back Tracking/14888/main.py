import sys
input = sys.stdin.readline
from itertools import permutations

def dfs(idx, r):
    if sum(cnt) == 0:
        global MIN, MAX
        MIN = min(MIN, r)
        MAX = max(MAX, r)

    for i in range(4):
        if cnt[i] <= 0:
            continue

        cnt[i] -= 1
        if i == 0:
            dfs(idx+1, r + A[idx+1])
        elif i == 1:
            dfs(idx+1, r - A[idx+1])
        elif i == 2:
            dfs(idx+1, r * A[idx+1])
        else:
            dfs(idx+1, int(r/A[idx+1]))
        cnt[i] += 1


n = int(input())
A = list(map(int, input().split()))
cnt = list(map(int, input().split()))
MIN, MAX = 10**9, -10**9
dfs(0, A[0])
print(MAX, MIN, sep="\n")