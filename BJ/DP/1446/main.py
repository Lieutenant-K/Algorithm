import sys
input = sys.stdin.readline

N, D = map(int, input().split())
shortcut = [tuple(map(int, input().split())) for _ in range(N)]
d = [i for i in range(D+1)]

for i in range(D+1):
    if i > 0:
        d[i] = min(d[i], d[i-1]+1)
    for start, end, cost in shortcut:
        if start == i and end <= D and end-start >= cost:
            d[end] = min(d[end], d[i]+cost)
print(d[D])