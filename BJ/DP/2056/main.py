import sys
input = sys.stdin.readline

n = int(input())
d = [0]*(n+1)
for i in range(1, n+1):
    s = list(map(int, input().split()))
    for k in s[1:]:
        d[i] = max(d[i], d[k]+s[0])
print(max(d))