import sys
input = sys.stdin.readline

s1 = input().rstrip()
s2 = input().rstrip()
d = [[0]*(len(s2)+1) for _ in range(len(s1)+1)]
r = 0
for i in range(1, len(s1)+1):
    for j in range(1, len(s2)+1):
        if s1[i-1] == s2[j-1]:
            d[i][j] = d[i-1][j-1] + 1
            r = max(r, d[i][j])
print(r)