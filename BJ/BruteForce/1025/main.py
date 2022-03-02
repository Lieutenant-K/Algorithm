import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = [list(input().rstrip()) for _ in range(n)]
ans = set([])
mx = -1
for i in range(n):
    for j in range(m):
        for di in range(-n+1, n):
            for dj in range(-m+1, m):
                r = s[i][j]
                ni, nj = i+di, j+dj
                # if not di and not dj:
                #     continue
                while (di or dj) and 0 <= ni < n and 0 <= nj < m:
                    r += s[ni][nj]
                    ni += di
                    nj += dj

                for k in range(1, len(r)+1):
                    v = int(r[:k])
                    sq = int(v ** 0.5)
                    if sq**2 == v:
                        mx = max(mx, v)
print(mx)