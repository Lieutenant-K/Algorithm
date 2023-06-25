import sys
input = sys.stdin.readline

n = int(input())
d = [[0]*10 for _ in range(n+1)]
d[1] = [0] + [1]*9
for i in range(1, n):
    for j in range(10):
        if j >= 1:
            d[i+1][j-1] += d[i][j]
        if j < 9:
            d[i+1][j+1] += d[i][j]
print(sum(d[n]) % 10**9)