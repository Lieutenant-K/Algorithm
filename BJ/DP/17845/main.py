import sys
input = sys.stdin.readline

n, k = map(int, input().split())
s = [tuple(map(int, input().split())) for _ in range(k)]
d = [[0]*(n+1) for _ in range(k+1)]
for i in range(1, k+1):
    for j in range(1, n+1):
        if s[i-1][1] > j:
            d[i][j] = d[i-1][j]
        else:
            d[i][j] = max(d[i-1][j], d[i-1][j-s[i-1][1]] + s[i-1][0])
print(d[k][n])