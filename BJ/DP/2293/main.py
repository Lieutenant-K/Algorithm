import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]
d = [0]*(k+1)
d[0] = 1
for c in coin:
    for i in range(1,k+1):
        if i-c < 0:
            continue
        d[i] += d[i-c]
print(d[k])