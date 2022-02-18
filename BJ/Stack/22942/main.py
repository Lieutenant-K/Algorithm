import sys
input = sys.stdin.readline

n = int(input())
S = []
for _ in range(n):
    x, r = map(int, input().split())
    S.append((x-r, x+r))
S.sort()
q = [S[0]]
for i in range(1, n):
    s, e = S[i]
    while q and s > q[-1][1]:
        q.pop()
    if not q:
        q.append(S[i])
        continue

    qs, qe = q[-1]
    if s == qs or e == qe or s == qe or (s < qe < e):
        print("NO")
        exit()
    q.append(S[i])
print("YES")