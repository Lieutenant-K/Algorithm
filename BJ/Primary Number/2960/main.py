import sys
input = sys.stdin.readline

n, k = map(int, input().split())
d = [False]*(n+1)
cnt = 0
for i in range(2, n+1):
    if not d[i]:
        j = 1
        while i*j <= n:
            if not d[i*j]:
                cnt += 1
                d[i*j] = True
                if cnt == k:
                    print(i*j)
            j += 1