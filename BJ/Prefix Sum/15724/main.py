import sys
input = sys.stdin.readline

N, M = map(int, input().split())
G = [[0]*(M+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
S = [[0]*(M+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, M+1):
        S[i][j] = G[i][j] + S[i-1][j] + S[i][j-1] - S[i-1][j-1]

for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    print(S[c][d] - S[c][b-1] - S[a-1][d] + S[a-1][b-1])