import sys
import pprint
input = sys.stdin.readline

n = int(input())
s = list(map(int, input().split()))
d = [[0]*21 for _ in range(n)]
d[0][s[0]] = 1

for i in range(1, n-1):
    for j in range(21):
        if j+s[i] < 21:
            d[i][j+s[i]] += d[i-1][j]
        if j-s[i] >= 0:
            d[i][j-s[i]] += d[i-1][j]
print(d[n-2][s[n-1]])