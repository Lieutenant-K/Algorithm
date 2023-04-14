import sys
input = sys.stdin.readline

s1 = input().rstrip()
s2 = input().rstrip()
s3 = input().rstrip()

n, m, k = len(s1), len(s2), len(s3)
d = [[[0]*(k+1) for _ in range(m+1)] for _ in range(n+1)]

for x in range(1, n+1):
    for y in range(1, m+1):
        for z in range(1, k+1):
            if s1[x-1] == s2[y-1] and s2[y-1] == s3[z-1]:
                d[x][y][z] = d[x-1][y-1][z-1] + 1
            else:
                d[x][y][z] = max(d[x-1][y][z], d[x][y-1][z], d[x][y][z-1])

print(d[n][m][k])