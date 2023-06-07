import sys
input = sys.stdin.readline

def find(n, recent):
    if n == 1:
        return recent

    r = n if visit[n] else recent
    if n % 2 == 0:
        return find(n // 2, r)
    else:
        return find((n-1) // 2, r)

N, Q = map(int, input().split())
x = [int(input()) for _ in range(Q)]
visit = [False]*(N+1)
for i in x:
    result = find(i, 0)
    if result == 0:
        visit[i] = True
    print(result)