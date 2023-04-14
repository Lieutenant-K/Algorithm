import sys
input = sys.stdin.readline

for _ in range(3):
    n = int(input())
    coin = [tuple(map(int, input().split())) for _ in range(n)]
    total = sum(list(map(lambda x:x[0]*x[1], coin)))

    if total % 2 != 0:
        print(0)
        continue

    m = total // 2
    d = [1] + [0]*m
    for c, k in coin:
        for i in range(m, c-1, -1):
            if d[i-c]:
                for j in range(k):
                    if i + c * j <= m:
                        d[i + c * j] = 1

    print(d[m])