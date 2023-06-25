import sys
input = sys.stdin.readline

def solution(n, x):
    if x in s:
        return 1

    i, j = 0, n-1
    while i < j:
        t = x - w[i] - w[j]
        if t != w[i] and t != w[j] and t in s:
            return 1
        if t < 0:
            j -= 1
        else:
            i += 1

    return 0

N, C = map(int, input().split())
w = sorted(list(map(int, input().split())))
s = set(w + [0])
print(solution(N, C))