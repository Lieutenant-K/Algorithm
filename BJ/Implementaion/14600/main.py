import sys
input = sys.stdin.readline

k = int(input())
x, y = map(int, input().split())
s = [[0]*(2**k) for _ in range(2**k)]
s[2**k-y][x-1] = -1
if k == 1:
    for i in range(2):
        for j in range(2):
            if s[i][j] == 0:
                s[i][j] = 1
        print(*s[i], sep=' ')
else:
    p = [(0, 0), (0, 2), (2, 0), (2, 2)]
    f = 0
    for n in range(4):
        a, b = p[n]
        for i in range(2):
            for j in range(2):
                if s[a+i][b+j] == -1:
                    f = n+1
                    continue
                s[a+i][b+j] = n+1

    for i in range(2):
        for j in range(2):
            if s[i+1][j+1] != f and s[i+1][j+1] != -1:
                s[i+1][j+1] = 5
    for i in range(4):
        print(*s[i], sep=' ')