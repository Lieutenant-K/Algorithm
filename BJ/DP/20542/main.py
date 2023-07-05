import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = input().rstrip()
ans = input().rstrip()
d = [[i]+[0]*m for i in range(n+1)]
d[0] = list(range(m+1))
for i in range(1, n+1):
    for j in range(1, m+1):
        if s[i-1] == ans[j-1] or (s[i-1] == 'v' and ans[j-1] == 'w') or (s[i-1] == 'i' and ans[j-1] in ['j', 'l']):
            d[i][j] = d[i-1][j-1]
        else:
            d[i][j] = min(d[i-1][j], d[i][j-1], d[i-1][j-1]) + 1
print(d[n][m])